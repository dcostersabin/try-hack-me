from base import BaseExecutor


class StopSubdomainScans(BaseExecutor):

    def commands(self):
        return ["docker stop $(docker ps -f 'name=thm_subdomain_*' -q)"]

    def post_execution(self):
        print(self.output)

    def process_error(self, e: Exception):
        pass
