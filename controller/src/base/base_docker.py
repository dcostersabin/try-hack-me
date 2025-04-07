from abc import ABC
from docker import DockerClient


class DockerBase(ABC):

    DEFAULT_CLIENT = "unix://var/run/docker.sock"

    def client(self):
        return DockerClient(base_url=self.DEFAULT_CLIENT)
