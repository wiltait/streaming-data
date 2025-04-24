# Guardian API to SQS Pipeline

Fetches articles from The Guardian API and publishes them to AWS SQS for processing.

## Features
- Searches The Guardian content API
- Filters by date range
- Publishes to AWS SQS queue
- PEP-8 compliant with unit tests

## Prerequisites
- Python 3.8+
- AWS account with SQS access
- Guardian API key

## Setup

1. Clone repository:
   ```bash
   git clone https://github.com/wiltait/streaming-data.git
   cd streaming-data
   ``` 
2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment:
   ```bash
   cp .env.example .env
   ```

Edit .env with your credentials:
    ```bash
    # Guardian API
    GUARDIAN_API_KEY=your_api_key_here

    # AWS Configuration
    AWS_ACCESS_KEY_ID=your_access_key_here
    AWS_SECRET_ACCESS_KEY=your_secret_key_here
    AWS_DEFAULT_REGION=eu-west-2
    SQS_QUEUE_URL=https://sqs.region.amazonaws.com/account-id/queue-name
    ```

## Usage

Run with default parameters:
    ```bash
    make run
    ```

Or with custom search:
    ```bash
    python src/main.py "climate change" --date_from 2023-01-01
    ```

## Testing
    ```bash
    make test
    ```
## Cleanup
    ```bash
    make clean
    ```