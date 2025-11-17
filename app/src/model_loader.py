import boto3
import logging
import os
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def get_s3_client():
    """
    Create an S3 client configured for S3.
    
    Returns:
        boto3.client: Configured S3 client for S3
    """
    return boto3.client(
        's3',
        endpoint_url=os.getenv('S3_ENDPOINT', 'http://172.0.0.1:9000'),
        aws_access_key_id=os.getenv('S3_ACCESS_KEY', 'S3admin'),
        aws_secret_access_key=os.getenv('S3_SECRET_KEY', 'S3admin'),
        region_name='us-east-1',
    )


def load_model_from_s3(bucket_name, model_key, download_path):
    """
    Downloads a model file from an S3-compatible storage (S3).

    Parameters:
    - bucket_name (str): The name of the S3 bucket.
    - model_key (str): The key (path) of the model file in the S3 bucket.
    - download_path (str): The local path where the model file will be saved.
    
    Returns:
        torch model: Loaded PyTorch model
    """
    s3 = get_s3_client()
    s3.download_file(bucket_name, model_key, download_path)
    logger.info(f"Model downloaded from s3://{bucket_name}/{model_key} to {download_path}")

    return True
        

