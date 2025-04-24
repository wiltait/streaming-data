from src.guardian_api import fetch_articles
from src.message_broker import SQSPublisher
import argparse

def main():
    """
    Main execution flow:
    1. Parses command line arguments
    2. Fetches articles from The Guardian API
    3. Publishes articles to AWS SQS queue
    """
    parser = argparse.ArgumentParser(description="Fetch articles from The Guardian and publish to AWS SQS")
    parser.add_argument("search_term", help="Seach term (ex: 'machine learning')")
    parser.add_argument("--date_from", help="Filter articles from this date format: YYYY-MM-DD")
    args = parser.parse_args()

    # Search for articles
    articles = fetch_articles(args.search_term, args.date_from)
    print(f"✅ {len(articles)} articles found.")

    # Publish in SQS
    publisher = SQSPublisher()
    for article in articles:
        message_id = publisher.publish_article(article)
        print(f"📬 Published: {article['webTitle']} (ID: {message_id})")

if __name__ == "__main__":
    main()