from base import BaseFactory
from services.port.check import CheckPortScan
from services.port.data import GetIPData
from services.port.scan import ScanPort


class PortScanService(BaseFactory):

    def __init__(self, cpu: int):
        self.data = {}
        self.checker: CheckPortScan = CheckPortScan()
        super(PortScanService, self).__init__(cpu=cpu)

    def pre_start(self):
        self.checker.start()
        ip_data = GetIPData()
        ip_data.start()
        self.data = ip_data.data

    def task(self, params):
        domain, ip = params
        if not self.checker.check(domain):
            ScanPort(domain=domain, ip=ip).start()

    def parameters(self):
        return self.data

    def process_responses(self, reponses):
        pass

    def post_start(self):
        pass
