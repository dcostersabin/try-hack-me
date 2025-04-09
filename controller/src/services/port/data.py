import re

import urllib3

from helpers import S3ClientHelper


class GetIPData(S3ClientHelper):

    def __init__(self, bucket="domains"):
        self.bucket = bucket
        self.data_files = set()
        self.data = set()
        self.ip_re = re.compile(
            (
                "(?:25[0-5]|2[0-4][0-9]|"
                "[01]?[0-9][0-9]?)\\.(?:25"
                "[0-5]|2[0-4][0-9]|[01]?[0-9]"
                "[0-9]?)\\.(?:25[0-5]|2[0-4][0-9]"
                "|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
            )
        )

    def start(self):
        self._run()

    def _run(self):
        self._fetch_bucket()

    def _fetch_bucket(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        objs = self.s3Client.list_objects(
            bucket_name=self.bucket,
            recursive=True,
        )

        _ = [
            self._process_file(obj.object_name)
            for obj in objs
            if "resp.txt" in obj.object_name
        ]

    def _process_file(self, name):
        obj = self.s3Client.get_object(
            bucket_name=self.bucket,
            object_name=name,
        )
        data = obj.data.decode()
        ips = set(re.findall(self.ip_re, data))
        domain = name.split("/")[0]
        domain = domain.replace("_", ".")
        _ = [self.data.add((domain, i)) for i in ips]
