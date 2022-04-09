from fileinput import filename
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def download_file(bucket, file, path="./"):
    try:
        s3.download_file(Bucket=bucket, Key=file,
                         Filename=path + file if path else file)
    except Exception as ex:
        print(ex)
        return
    print(f"file {file} has been downloaded successfully")


if __name__ == "__main__":
    download_file("devpyth-200", "Shanghai.png",)
