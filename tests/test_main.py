import unittest
from unittest.mock import patch, MagicMock
import argparse

from src.main import main

class TestMain(unittest.TestCase):
    @patch('src.main.fetch_articles')  # Patch where it's USED (in main.py)
    @patch('src.main.SQSPublisher')    # Same for the publisher
    def test_main_success(self, mock_publisher, mock_fetch):
        """Test main execution flow with mocks"""
        # Setup mock args
        args = argparse.Namespace(
            search_term="test",
            date_from=None
        )
        
        # Setup mock return values
        mock_fetch.return_value = [{
            "webTitle": "Test", 
            "webUrl": "url", 
            "webPublicationDate": "date"
        }]
        
        mock_pub_instance = MagicMock()
        mock_pub_instance.publish_article.return_value = "msg123"
        mock_publisher.return_value = mock_pub_instance

        # Patch argparse to return our mock args
        with patch('argparse.ArgumentParser.parse_args', 
                 return_value=args):
            with patch('builtins.print'):  # Suppress print output
                main()

        # Verify calls
        mock_fetch.assert_called_once_with("test", None)
        mock_pub_instance.publish_article.assert_called_once_with({
            "webTitle": "Test",
            "webUrl": "url",
            "webPublicationDate": "date"
        })

if __name__ == '__main__':
    unittest.main()