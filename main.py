import boto3
import os

def main():
    mobile_no = os.environ["INPUT_MOBILE_NO"]
    aws_key_id = os.environ["INPUT_AWS_KEY_ID"]
    aws_key_access = os.environ["INPUT_AWS_KEY_ACCESS"]
    client = boto3.client('sns', 'us-east-1', aws_access_key_id=aws_key_id, aws_secret_access_key=aws_key_access)
    topic = client.create_topic(Name="notifications")
    topic_arn = topic['TopicArn']
    client.subscribe(TopicArn=topic_arn, Protocol='sms', Endpoint=mobile_no)
    msg = "A new push just happened in your repo."
    client.publish(TopicArn=topic_arn, Message=msg)


if __name__ == "__main__":
    main()
