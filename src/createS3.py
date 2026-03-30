import logging
import boto3
from botocore.exceptions import ClientError

class AWS:

    def __init__(self, bucket_name: str):
        self.initial_bucket_name = bucket_name
        self.s3_client = boto3.client("s3")
        self.sts_client = boto3.client("sts")


    def create_bucket(self):
        try:
            new_bucket = self.create_name_bucket()
            self.s3_client.create_bucket(Bucket=new_bucket["name_bucket"])
            print(f"S3 bucket {new_bucket["name_bucket"]} created successfully in region {new_bucket["region"]}")
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def create_name_bucket(self):
        
        region_default = self.s3_client.meta.region_name
        response = self.sts_client.get_caller_identity()
        account_id = response["Account"]
    
        
        name_bucket = f"{self.initial_bucket_name}-{account_id}-{region_default}"
        
        return {"name_bucket":name_bucket, "region": region_default}


if __name__ == "__main__":

    aws = AWS("static-site-bucket")
    aws.create_bucket()