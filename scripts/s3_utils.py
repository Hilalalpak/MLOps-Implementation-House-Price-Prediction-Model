# s3_utils.py
import boto3
import pandas as pd
import io
import os
import logging
from botocore.config import Config
from dotenv import load_dotenv
import sys
from pathlib import Path

load_dotenv('/home/jovyan/work/housing-mlops/.env')

ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
S3_ENDPOINT = os.getenv('S3_ENDPOINT_URL')

def get_s3_client():
    s3 = boto3.client('s3',
                    endpoint_url='http://172.22.0.9:9000',
                    aws_access_key_id=ACCESS_KEY,
                    aws_secret_access_key=SECRET_KEY,
                    config=Config(signature_version='s3v4',
                                 s3={'addressing_style': 'path'}))
    return s3

def get_s3_resource():
    s3_res = boto3.resource('s3',
                          endpoint_url='http://172.22.0.9:9000',
                          aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY,
                          config=Config(signature_version='s3v4',
                                       s3={'addressing_style': 'path'}))
    return s3_res

def create_bucket(bucket_name):
    s3_res = get_s3_resource()
    try:
        s3_res.create_bucket(Bucket=bucket_name)
        logging.info(f"Bucket '{bucket_name}' created.")
        return True
    except Exception as e:
        logging.error(f"Bucket creation error: {e}")
        return False

def save_df_to_s3(df, bucket, key, index=False):
    s3_res = get_s3_resource()
    try:
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=index)
        s3_res.Object(bucket, key).put(Body=csv_buffer.getvalue())
        logging.info(f"'{key}' saved to '{bucket}' bucket.")
        return True
    except Exception as e:
        logging.error(f"S3 save error: {e}")
        return False

def load_df_from_s3(bucket, key, index_col=None, usecols=None):
    s3_client = get_s3_client()
    try:
        obj = s3_client.get_object(Bucket=bucket, Key=key)
        return pd.read_csv(obj['Body'], index_col=index_col, usecols=usecols)
    except Exception as e:
        logging.error(f"S3 load error: {e}")
        return None
