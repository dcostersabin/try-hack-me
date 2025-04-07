from abc import ABC, abstractmethod


class BaseFactory(ABC):

    @abstractmethod
    def start(self):
        raise NotImplementedError("create not implemented")
