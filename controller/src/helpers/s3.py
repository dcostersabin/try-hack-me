from os import getenv

from minio import Minio


class S3ClientHelper:
    @property
    def s3Client(self):

        return Minio(
            endpoint=getenv("SERVER_URL").replace(
                "https://",
                "",
            ),
            access_key=getenv("ACCESS_KEY"),
            secret_key=getenv("SECRET_KEY"),
            cert_check=False,
        )
