import boto3
import os

def main():
    mobile_no = os.environ["INPUT_MOBILE_NO"]
    aws_key_id = os.environ["INPUT_AWS_KEY_ID"]
    aws_key_access = os.environ["INPUT_AWS_KEY_ACCESS"]
    client = boto3.client(
        'sns',
        'us-east-1',
        aws_access_key_id=aws_key_id,
        aws_secret_access_key=aws_key_access
    )
    msg = "A push just happened to you repo"
    client.publish(PhoneNumber=mobile_no, Message=msg)

if __name__ == "__main__":
    main()
