import requests
import data_config
import logging
import boto3

logger = logging.getLogger()

DILBERT_URL = "http://dilbert-api.glitch.me/json"
SECRET_ID = "nike_slack_webhook_urls"
SLACK_CHANNEL = "test_space"
TABLE_NAME = "nike_daily_smile_tracking"
TABLE = boto3.resource('dynamodb').Table(TABLE_NAME)
AWS_REGION = "us-west-2"

# get slack webhook from secretsmanager
# Create a Secrets Manager client
def get_slack_webhook_url():
    logger.info("retrieving webhook from secretsmanager")
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=AWS_REGION
    )
    secretsmanager_response = client.get_secret_value(
        SecretId=SECRET_ID
    )
    return secretsmanager_response[SLACK_CHANNEL]


def get_last_comic_metadata():
    db_entry_key = {"comic_name": "dilbert"}
    db_item = TABLE.get_item(Key=db_entry_key)
    return db_item["output"]


def save_comic_metadata(output):
    db_entry = {
        "comic_name": "dilbert",
        "output": output
    }
    TABLE.put_item(Item=db_entry)


dilbert_response = requests.get(url = dilbert_url)
data = dilbert_response.json()
output = f"Title: {str(data['title'])}\nhttps:{data['image']}
logger.info(f"Output: {output}")

if get_last_comic_metadata() == output:
    # send to slack
    daily_headers = { "content-type": "application/json" }
    slack_response = requests.post(url=get_slack_webhook_url(), data=str({"text": output}), headers=daily_headers,)
    # save metadata
    save_comic_metadata(output)
