from botocore.vendored import requests
import logging
import boto3
import json


XKCD_URL = "https://xkcd.com/info.0.json"
SECRET_ID = "nike_slack_webhook_urls"
SLACK_CHANNEL = "test_space"
TABLE_NAME = "nike_daily_smile_tracking"
TABLE = boto3.resource('dynamodb').Table(TABLE_NAME)
AWS_REGION = "us-west-2"
logger = logging.getLogger()

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
    secret_string = json.loads(secretsmanager_response["SecretString"])
    return secret_string[SLACK_CHANNEL]


def get_last_comic_metadata():
    db_entry_key = {"comic_name": "xkcd"}
    db_item = TABLE.get_item(Key=db_entry_key)
    if not db_item.get("Item") or not db_item["Item"].get("output"):
        return None
    return db_item["Item"]["output"]


def save_comic_metadata(output):
    db_entry = {
        "comic_name": "xkcd",
        "output": output
    }
    TABLE.put_item(Item=db_entry)
    
    
def lambda_handler(event, context):
    xkcd_response = requests.get(url=XKCD_URL)
    data = xkcd_response.json()
    output = "Comic Number: " + str(data['num']) + "\nTitle: " + data['title'] + "\nAlt Text: " + data['alt'] + "\n" + data['img']
    logger.info(f"Output: {output}")
    
    if get_last_comic_metadata() != output:
        # send to slack
        daily_headers = { "content-type": "application/json" }
        slack_response = requests.post(url=get_slack_webhook_url(), data=str({"text": output}), headers=daily_headers)
        # save metadata
        save_comic_metadata(output)
        return f"Published comic. Slack response: {slack_response.status_code}"
    return "no new comic"

