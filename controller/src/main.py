from argparse import Namespace

from base import parser
from services import ServiceEnum as S
from services import ServiceFactory
from services.port import StopPortScans
from services.subdomain import StopSubdomainScans


class Cli:

    def __init__(self, params: Namespace):
        self.params: Namespace = params

    def start(self):
        self._run()

    def _run(self):
        if self.params.subdomain:
            ServiceFactory.get_service(
                cpu=self.params.cpu,
                name=S.SUBDOMAIN,
            ).start()

        if self.params.port:
            ServiceFactory.get_service(
                cpu=self.params.cpu,
                name=S.PORT,
            ).start()

        if self.params.stop_subdomain:
            StopSubdomainScans().start()

        if self.params.stop_portscan:
            StopPortScans().start()


if __name__ == "__main__":
    ar = parser.parse_args()
    Cli(params=ar).start()
