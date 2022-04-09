import boto3
from botocore.exceptions import ClientError

s3 = boto3.client("s3")


def generate_bucket(bucket_name):
    try:
        response = s3.head_bucket(Bucket=bucket_name)
    except Exceptions as ex:
        print(ex)
        return False
    status_code = response["ResponseMetadata"]["HTTPStatusCode"]
      if status_code == 200:
          return True
        return False


def create_bucket(bucket_name):
        try:
            s3.create_bucket(Bucket=bucket_name)
            print(f"Bucket named {bucket_name} has been created successfully")
        except Exception as ex:
            print(f"Couldn't create a bucket: {ex}")
    else:
        print(f"{bucket_name} already exists")


if __name__ == "__main__":
    create_bucket("ziziko-bucket")
