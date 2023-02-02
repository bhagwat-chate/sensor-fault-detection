import os, sys
from sensor.exception import SensorException
from sensor.logger import logging

class S3Sync:

    def sync_folder_to_s3(self, aws_bucket_url):
        command = f"aws s3 sync {folder} {aws_bucket_url}"
        os.system(command)

    def sync_folder_from_s3(self, folder_aws_bucket_url):
        command = f"aws sync {aws_bucket_url} {folder}"
        os.system(command)
