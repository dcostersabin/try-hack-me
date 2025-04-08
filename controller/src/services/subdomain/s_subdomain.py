from base import BaseFactory
from services.subdomain.check import CheckDomainScan
from services.subdomain.scan import ScanDomain
from services.subdomain.targets import GetScanTargets


class SubdomainService(BaseFactory, GetScanTargets):

    def __init__(self, cpu: int):
        self.checker: CheckDomainScan = CheckDomainScan()
        super(SubdomainService, self).__init__(cpu=cpu)

    def pre_start(self):
        self.checker.start()

    def task(self, params):
        if not self.checker.check(params):
            ScanDomain(domain=params).start()

    def parameters(self):
        return [i for i in self.domains]

    def process_responses(self, reponses):
        pass

    def post_start(self):
        pass
