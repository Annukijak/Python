import boto3

s3 = boto3.client('s3')

def get_buckets(bucketName = ""):
    response = s3.list_buckets()['Buckets']
    if bucketName:
        match = [s for s in response if s['Name'].__contains__(bucketName.lower())]
        if match:
            print("Found matching buckets:")
            for bucket in match:
                print(f'{bucket["Name"]}')
        else:
            print("There are no buckets under this name!")
    else:
        for bucket in response:
            print(f'{bucket["Name"]}')

if __name__ == '__main__':
    get_buckets("prod")
