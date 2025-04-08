from os import getenv

import urllib3
from minio import Minio


class CheckDomainScan:

    def __init__(self, bucket="domains"):
        self.data = None
        self.bucket = bucket

    def start(self) -> bool:
        return self._run()

    def _run(self):
        self._get_domains()

    def _get_domains(self):
        client = Minio(
            endpoint=getenv("SERVER_URL").replace(
                "https://",
                "",
            ),
            access_key=getenv("ACCESS_KEY"),
            secret_key=getenv("SECRET_KEY"),
            cert_check=False,
        )

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        objs = client.list_objects(bucket_name=self.bucket)
        self.data = [i.object_name for i in objs]

    def check(self, domain: str):
        domain = domain.replace(".", "_")
        return f"{domain}/" in self.data
