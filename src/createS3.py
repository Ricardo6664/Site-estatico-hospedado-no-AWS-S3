import logging
import json
import os
import sys
import boto3
from botocore.exceptions import ClientError


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)


class AWS:

    def __init__(self, bucket_name: str):
        self.initial_bucket_name = bucket_name
        self.s3_client = boto3.client("s3")
        self.sts_client = boto3.client("sts")
        self.separate_message = "#############################"


    def create_bucket(self):
        try:
            new_bucket = self.create_name_bucket()
            self.s3_client.create_bucket(Bucket=new_bucket["name_bucket"])
            logging.info(f"S3 bucket {new_bucket["name_bucket"]} created successfully in region {new_bucket["region"]}")
            self.upload_files(new_bucket["name_bucket"])
        except ClientError as e:
            logging.error(e)
            return False
        return new_bucket["name_bucket"]

    def create_name_bucket(self):
        try:
            region_default = self.s3_client.meta.region_name
            response = self.sts_client.get_caller_identity()
            account_id = response["Account"]
            name_bucket = f"{self.initial_bucket_name}-{account_id}-{region_default}"
            return {"name_bucket":name_bucket, "region": region_default}
        
        except Exception as e:
            logging.error(e)
            sys.exit(1)

    def createS3public(self):
        try:
            name = aws.create_bucket()
            self.s3_client.delete_public_access_block(Bucket= name)
            logging.info("Public access block remove successfully")
            return name
        except Exception as e:
            logging.error(e)
    
    def createbucketpoliy(self):
        bucket = self.createS3public()
        arn = f"arn:aws:s3:::{bucket}/*"
        policy = {
                "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Sid": "PublicReadGetObject",
                            "Effect": "Allow",
                            "Principal": "*",
                            "Action": "s3:GetObject",
                            "Resource": arn
                        }
                    ]
                }
        policy_string = json.dumps(policy)
        try:
            self.s3_client.put_bucket_policy(
                Bucket = bucket,
                Policy = policy_string
            )
            logging.info("Role added successfully")
            return bucket
        except Exception as e:
            logging.error("Error in add role", e)
            
    def configure_static_website(self):
        try:
            bucket = self.createbucketpoliy()
            self.s3_client.put_bucket_website(
            Bucket=bucket,
            WebsiteConfiguration={
                'ErrorDocument': {'Key': 'error.html'},
                'IndexDocument': {'Suffix': 'index.html'},
            })
            logging.info("Static Website habilited")
        except Exception as e:
            logging.error(e)

    def upload_files(self, BUCKET_NAME: str):
        try:
            logging.info("Enviando os arquivos")
            files = ['index.html', 'error.html']
            for index, name in enumerate(files):
                path_complete = os.path.join(os.getcwd(),files[index])
                self.s3_client.upload_file(path_complete, BUCKET_NAME, name, ExtraArgs={'ContentType': 'text/html'})
                logging.info(f"File {name} created successfully")
        except Exception as e:
            logging.error(e)
            
if __name__ == "__main__":

    aws = AWS("static-site-bucket")
    aws.configure_static_website()
    