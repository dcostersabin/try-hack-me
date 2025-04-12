from os import getenv

from base import BaseExecutor


class ScanDomain(BaseExecutor):

    def __init__(self, domain: str):
        self.domain = domain
        self.clean_domain = domain.replace(".", "_")
        super(ScanDomain, self).__init__()

    @property
    def name(self):
        return f"thm_subdomain_{self.clean_domain}"

    def commands(self):
        return [
            (
                f"docker run --rm --name {self.name} -e MC_INSECURE=true "
                f"-e SERVER_URL={getenv('SERVER_URL')} "
                f"-e ACCESS_KEY={getenv('ACCESS_KEY')} "
                f"-e SECRET_KEY={getenv('SECRET_KEY')} "
                f"ghcr.io/dcostersabin/thm_subdomain:latest {self.domain}"
            )
        ]

    def post_execution(self):
        print(self.output)

    def process_error(self, e: Exception):
        pass
