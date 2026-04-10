import boto3
import logging
import webbrowser

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

class CloudFront:
    def __init__(self, url: str):
        self.url_website = url
        self.cloudfront = boto3.client('cloudfront')

    def createDistribution(self):
        try:
            response = self.cloudfront.create_distribution(
                DistributionConfig={
                    "CallerReference": "my-site-ref-001",
                    "Comment": "My static website distribution",
                    "Enabled": True,
                    "DefaultRootObject": "index.html",
                    
                    "Origins": {
                        "Quantity": 1,
                        "Items": [{
                            "Id": "S3-Website-Origin",
                            "DomainName": self.url_website,
                            "CustomOriginConfig": {
                                "HTTPPort": 80,
                                "HTTPSPort": 443,
                                "OriginProtocolPolicy": "http-only",
                            }
                        }]
                    },
                    
                    "DefaultCacheBehavior": {
                        "TargetOriginId": "S3-Website-Origin",
                        "ViewerProtocolPolicy": "redirect-to-https",
                        "AllowedMethods": {
                            "Quantity": 2,
                            "Items": ["GET", "HEAD"],
                        },
                        "CachePolicyId": "658327ea-f89d-4fab-a63d-7e88639e58f6",
                        "Compress": True,
                    },
                    "CustomErrorResponses":{
                        "Quantity": 1,
                        "Items": [{
                            "ErrorCode": 404,
                            "ResponsePagePath": "/error.html",
                            "ResponseCode": "404",
                            "ErrorCachingMinTTL": 300,
                        }]
                    }
                }
            )
            dist = response["Distribution"]
            url_cloudfront = f"https://{dist["DomainName"]}"
            logging.info("\n\nCloudfront created successfully\n")
            logging.info(f"Id: {dist["Id"]}")
            logging.info(f"Status: {dist["Status"]}")
            logging.info(f"URL: {url_cloudfront}\n\n")
            
            logging.info("The website is opening in your browser, await a minuto...")
            webbrowser.open(url_cloudfront)
            
            return dist
        except Exception as e:
            logging.error(f"Had a error. It is {e}")
            return e