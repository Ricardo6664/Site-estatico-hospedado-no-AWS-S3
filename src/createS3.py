import logging
import json
import os
import mimetypes
import boto3
from botocore.exceptions import ClientError


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class AWS:

    def __init__(self, bucket_name: str):
        self.initial_bucket_name = bucket_name
        self.s3_client = boto3.client("s3")
        self.sts_client = boto3.client("sts")


    def create_bucket(self):
        try:
            new_bucket = self.create_name_bucket()
            self.s3_client.create_bucket(Bucket=new_bucket["name_bucket"])
            logging.info(f"S3 bucket {new_bucket["name_bucket"]} created successfully in region {new_bucket["region"]}")
        except ClientError as e:
            logging.error(e)
            return False
        return new_bucket["name_bucket"]

    def create_name_bucket(self):
        
        region_default = self.s3_client.meta.region_name
        response = self.sts_client.get_caller_identity()
        account_id = response["Account"]
        name_bucket = f"{self.initial_bucket_name}-{account_id}-{region_default}"
        return {"name_bucket":name_bucket, "region": region_default}
    
    def createS3public(self):
        name = aws.create_bucket()
        self.s3_client.delete_public_access_block(Bucket= name)
        logging.info("Bloqueio de acesso público removido com sucesso")
        return name
    
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
            logging.info("Política adicionada com sucesso")
            return bucket
        except Exception as e:
            print("Erro ao adicionar a política", e)
            
    def configure_static_website(self):
        bucket = self.createbucketpoliy()
        self.s3_client.put_bucket_website(
        Bucket=bucket,
        WebsiteConfiguration={
            'ErrorDocument': {'Key': 'error.html'},
            'IndexDocument': {'Suffix': 'index.html'},
        })
        logging.info("Hospedagem de site estático habilitado")
        
    def upload_files(self, BUCKET_NAME: str):
        logging.info("Enviando os arquivos")
        files = ['index.html', 'error.html']

if __name__ == "__main__":

    aws = AWS("static-site-bucket")
    aws.configure_static_website()