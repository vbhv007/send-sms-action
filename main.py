import boto3
import os

def main():
    client = boto3.client('sns', 'us-east-1')
    mobile_no = os.environ["INPUT_MOBILE_NO"]
    msg = "A push just happened to you repo"
    client.publish(PhoneNumber=mobile_no, Message=msg)

if __name__ == "__main__":
    main()
