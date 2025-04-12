from base import BaseExecutor


class StopPortScans(BaseExecutor):

    def commands(self):
        return ["docker stop $(docker ps -f 'name=thm_port_scanner*' -q)"]

    def post_execution(self):
        print(self.output)

    def process_error(self, e: Exception):
        pass
