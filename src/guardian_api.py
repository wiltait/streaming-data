import os
import requests
from dotenv import load_dotenv

load_dotenv()

GUARDIAN_API_KEY = os.getenv("GUARDIAN_API_KEY")
GUARDIAN_API_URL = "https://content.guardianapis.com/search"

def fetch_articles(search_term, date_from=None):
    """
    Fetches articles from The Guardian API based on search criteria.
    
    Args:
        search_term (str): Term to search for in articles.
        date_from (str, optional): Start date for articles (YYYY-MM-DD format). Defaults to None.
    
    Returns:
        list: List of formatted article dictionaries containing:
              - webTitle: Article title
              - webUrl: Article URL
              - webPublicationDate: Publication timestamp
    """
    params = {
        "q": search_term,
        "api-key": os.getenv("GUARDIAN_API_KEY"),
        "show-fields": "webPublicationDate,webTitle,webUrl",
        "page-size": 10
    }
    if date_from:
        params["from-date"] = date_from

    response = requests.get(GUARDIAN_API_URL, params=params)
    articles = response.json().get("response", {}).get("results", [])
    
    return [{
        "webTitle": article["webTitle"],
        "webUrl": article["webUrl"],
        "webPublicationDate": article["webPublicationDate"]
    } for article in articles]