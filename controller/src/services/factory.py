from enum import Enum

from base import BaseFactory
from services.subdomain import SubdomainService


class ServiceEnum(Enum):
    SUBDOMAIN = "subdomain"


class ServiceFactory:

    @staticmethod
    def get_service(cpu: int, name: ServiceEnum) -> BaseFactory:

        match name:
            case ServiceEnum.SUBDOMAIN:
                return SubdomainService(cpu=cpu)
