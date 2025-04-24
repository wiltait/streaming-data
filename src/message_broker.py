import boto3
import os
import json
from dotenv import load_dotenv

load_dotenv()

class SQSPublisher:
    """
    Handles publishing messages to AWS SQS queue.
    """
    def __init__(self):
        """
        Initializes SQS client using credentials from environment variables.
        """
        self.sqs = boto3.client(
            'sqs',
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_DEFAULT_REGION")
        )
        self.queue_url = os.getenv("SQS_QUEUE_URL")

    def publish_article(self, article):
        """
        Publishes an article to SQS queue.
        
        Args:
            article (dict): Article data to publish
        
        Returns:
            str: Message ID if successful, None otherwise
        """
        try:
            response = self.sqs.send_message(
                QueueUrl=self.queue_url,
                MessageBody=json.dumps(article))
            return response['MessageId']
        except Exception as e:
            print(f"Error publishing to SQS: {e}")
            return None