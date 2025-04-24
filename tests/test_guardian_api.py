import unittest
from unittest.mock import patch, Mock
from src.guardian_api import fetch_articles
import os

class TestGuardianAPI(unittest.TestCase):
    @patch.dict(os.environ, {"GUARDIAN_API_KEY": "test_key"})
    @patch('requests.get')
    def test_fetch_articles_success(self, mock_get):
        """Test successful API response with mock data"""
        # Setup mock response
        mock_response = Mock()
        mock_response.json.return_value = {
            "response": {
                "results": [
                    {
                        "webTitle": "Test Article",
                        "webUrl": "https://example.com",
                        "webPublicationDate": "2023-01-01T00:00:00Z"
                    }
                ]
            }
        }
        mock_get.return_value = mock_response

        # Call function
        articles = fetch_articles("test", "2023-01-01")
        
        # Assertions
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0]["webTitle"], "Test Article")
        mock_get.assert_called_once()

    @patch.dict(os.environ, {"GUARDIAN_API_KEY": "test_key"})
    @patch('requests.get')
    def test_fetch_articles_empty(self, mock_get):
        """Test empty API response"""
        mock_response = Mock()
        mock_response.json.return_value = {"response": {"results": []}}
        mock_get.return_value = mock_response

        articles = fetch_articles("empty")
        self.assertEqual(len(articles), 0)

    @patch.dict(os.environ, {"GUARDIAN_API_KEY": "test_key"})
    @patch('requests.get')
    def test_fetch_articles_error(self, mock_get):
        """Test API error handling"""
        mock_get.side_effect = Exception("API Error")
        with self.assertRaises(Exception):
            fetch_articles("error")

if __name__ == '__main__':
    unittest.main()