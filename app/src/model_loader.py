import boto3
import logging

logger = logging.getLogger(__name__)



def download_model_from_s3(bucket_name, model_key, download_path):
    """
    Downloads a model file from an S3 bucket.

    Parameters:
    - bucket_name (str): The name of the S3 bucket.
    - model_key (str): The key (path) of the model file in the S3 bucket.
    - download_path (str): The local path where the model file will be saved.
    """
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, model_key, download_path)
    logger.info(f"Model downloaded from s3://{bucket_name}/{model_key} to {download_path}")