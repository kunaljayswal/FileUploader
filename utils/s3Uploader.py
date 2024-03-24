import boto3
import config

def upload_to_s3(file_data, file_name):

    print(file_name + "inside upload to s3")

    region_name = config.s3_region_name
    print(region_name)

    # Upload file to AWS S3
    s3 = boto3.client('s3', aws_access_key_id=config.aws_key_id, 
                      aws_secret_access_key=config.aws_access_key, region_name=region_name)
    bucket_name = config.aws_bucket
    s3_key = f"files/{file_name}"

    s3.upload_fileobj(
        Fileobj=file_data,
        Bucket=bucket_name,
        Key=s3_key
    )

    # Constructing the S3 object URL
    s3_object_url = f"https://{bucket_name}.s3.amazonaws.com/{s3_key}"

    return s3_object_url