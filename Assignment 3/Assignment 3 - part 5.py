import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')


def upload_file(input, bucket, output):
    with open(input, 'rb') as file:
        try:
            s3.upload_file(file, bucket, output)
        except Exception as ex:
            print(ex)
            return
        print("file has been uploaded successfully")


if __name__ == "__main__":
    upload_file("Shanghai.png","devpyth-200", "fons1-dev1")
