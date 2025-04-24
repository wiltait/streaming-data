import os
import requests
from dotenv import load_dotenv

load_dotenv()

GUARDIAN_API_KEY = os.getenv("GUARDIAN_API_KEY")
GUARDIAN_API_URL = "hhtps://content.guardianapis.com/search"

def fetch_articles(search_term, date_from=None):
    params = {
        "q": search_term,
        "api-key": GUARDIAN_API_KEY,
        "show-fields": "webPublicationDate,webTitle,webURL",
        "page-size": 10
    }
    if date_from:
        params["from-date"] = date_from

    response = requests.get(GUARDIAN_API_URL, params=params)
    if response.status_code == 200:
        return response.json().get("response", {}).get("results", [])
    else:
        raise Exception(f"Erro ao buscar artigo: {response.status_code}")