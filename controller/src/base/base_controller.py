from abc import ABC, abstractmethod
from typing import Sequence, Tuple
from multiprocessing import Pool, cpu_count


class BaseController(ABC):

    def __init__(self, cpu: int = 4, timeout: int = 30):
        self.timeout: int = timeout * 60
        self.cpu: int = cpu

    def start(self):
        self._run()

    @abstractmethod
    def task(self, *args, **kwargs):
        raise NotImplementedError("Start not implemented")

    @abstractmethod
    def parameters(self, *args, **kwargs) -> Sequence[Tuple]:
        raise NotImplementedError("Parameters Not Implemented")

    @abstractmethod
    def process_responses(self, responses: list):
        raise NotImplementedError("Process Response Not Implemented")

    def _run(self):
        with Pool(processes=min(self.cpu, cpu_count())) as p:
            process = [p.apply_async(self.task) for i in self.parameters()]
            status = [res.get(timeout=self.timeout) for res in process]
            _ = [self.process_responses(i) for i in status]
