from abc import ABC, abstractmethod
from multiprocessing import Pool, cpu_count


class BaseFactory(ABC):

    def __init__(self, cpu: int = 4, timeout: int = 30):
        self.timeout: int = timeout * 60
        self.cpu: int = cpu
        super(BaseFactory, self).__init__()

    def start(self):
        self._run()

    @abstractmethod
    def task(self, param):
        raise NotImplementedError("Start not implemented")

    @abstractmethod
    def parameters(self) -> list:
        raise NotImplementedError("Parameters Not Implemented")

    @abstractmethod
    def process_responses(self, responses: list):
        raise NotImplementedError("Process Response Not Implemented")

    def _run(self):
        with Pool(processes=min(self.cpu, cpu_count())) as p:
            process = [
                p.apply_async(self.task, (i,)) for i in self.parameters()
            ]  # noqa
            status = [res.get(self.timeout) for res in process]
            _ = [self.process_responses(i) for i in status]
