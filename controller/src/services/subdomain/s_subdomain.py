from base import BaseFactory
from services.subdomain.scan import ScanDomain
from services.subdomain.targets import GetScanTargets


class SubdomainService(BaseFactory, GetScanTargets):

    def __init__(self, cpu: int):
        super(SubdomainService, self).__init__(cpu=cpu)

    def task(self, params):
        ScanDomain(domain=params).start()

    def parameters(self):
        return [i for i in self.domains]

    def process_responses(self, reponses):
        print(reponses)
