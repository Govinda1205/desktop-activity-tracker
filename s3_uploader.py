# s3_uploader.py
import boto3
import os
from botocore.exceptions import NoCredentialsError

class S3Uploader:
    def __init__(self, bucket_name):
        self.s3 = boto3.client('s3')
        self.bucket_name = bucket_name

    def upload_file(self, file_path):
        try:
            self.s3.upload_file(
                file_path, 
                self.bucket_name, 
                os.path.basename(file_path),
                ExtraArgs={'ServerSideEncryption': 'AES256'}
            )
            print(f"File {file_path} uploaded successfully")
        except FileNotFoundError:
            print(f"The file {file_path} was not found")
        except NoCredentialsError:
            print("Credentials not available")
