import urllib3

from helpers import S3ClientHelper


class CheckDomainScan(S3ClientHelper):

    def __init__(self, bucket="domains"):
        self.data = None
        self.bucket = bucket

    def start(self) -> bool:
        return self._run()

    def _run(self):
        self._get_domains()

    def _get_domains(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        objs = self.s3Client.list_objects(bucket_name=self.bucket)
        self.data = [i.object_name for i in objs]

    def check(self, domain: str):
        domain = domain.replace(".", "_")
        return f"{domain}/" in self.data
