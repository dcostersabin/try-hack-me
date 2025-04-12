from os import getenv

from base import BaseExecutor


class ScanPort(BaseExecutor):

    def __init__(self, domain: str, ip: str):
        self.domain = domain
        self.ip = ip
        super(ScanPort, self).__init__()

    @property
    def clean_ip(self):
        return self.ip.replace(".", "_")

    @property
    def name(self):
        return f"thm_port_scanner_{self.clean_ip}"

    def commands(self):
        return [
            (
                f"docker run --rm --name {self.name} -e MC_INSECURE=true "
                f"-e SERVER_URL={getenv('SERVER_URL')} "
                f"-e ACCESS_KEY={getenv('ACCESS_KEY')} "
                f"-e SECRET_KEY={getenv('SECRET_KEY')} "
                f"ghcr.io/dcostersabin/thm_port_scanner:latest "
                f"{self.domain} {self.ip}"
            )
        ]

    def post_execution(self):
        print(self.output)

    def process_error(self, e: Exception):
        print(e)
