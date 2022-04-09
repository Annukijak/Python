import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def delete_bucket(bucket, file):
    try:
        s3.delete_object(Bucket=bucket, Key=file)
    except ClientError as e:
        print(e)
        return
    print("file has been deleted successfully")


if __name__ == "__main__":
    delete_bucket("devpyth-200", "Shanghai.png")
