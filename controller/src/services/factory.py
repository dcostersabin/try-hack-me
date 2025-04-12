from enum import Enum

from base import BaseFactory
from services.port import PortScanService
from services.subdomain import SubdomainService


class ServiceEnum(Enum):
    SUBDOMAIN = "subdomain"
    PORT = "port"


class ServiceFactory:

    @staticmethod
    def get_service(cpu: int, name: ServiceEnum) -> BaseFactory:

        match name:
            case ServiceEnum.SUBDOMAIN:
                return SubdomainService(cpu=cpu)
            case ServiceEnum.PORT:
                return PortScanService(cpu=cpu)
