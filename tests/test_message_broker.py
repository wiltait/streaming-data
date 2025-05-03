# tests/test_message_broker.py
import unittest
from unittest.mock import patch
from src.message_broker import SQSPublisher
import os
from dotenv import load_dotenv

load_dotenv()

class TestSQSPublisherIntegration(unittest.TestCase):
    """Integration tests for SQS connectivity (requires AWS credentials)"""
    
    @classmethod
    def setUpClass(cls):
        cls.queue_url = os.getenv("SQS_QUEUE_URL")
        if not cls.queue_url:
            raise unittest.SkipTest("SQS_QUEUE_URL not set in .env")

    def test_real_sqs_connection(self):
        """End-to-end test with real SQS (requires AWS access)"""
        publisher = SQSPublisher()
        test_msg = {"test": "Integration test"}
        
        # Test publish
        message_id = publisher.publish_article(test_msg)
        self.assertIsNotNone(message_id)
        

if __name__ == "__main__":
    unittest.main()