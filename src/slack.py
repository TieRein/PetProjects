from botocore.vendored import requests
import logging
import boto3
import json

logger = logging.getLogger()

AWS_REGION = "us-west-2"
SECRET_ID = "nike_slack_webhook_urls"
SLACK_CHANNEL = "test_space"


def get_webhook_url(slack_channel):
    logger.info("retrieving webhook from secretsmanager")
    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager",
        region_name=AWS_REGION,
    )
    secretsmanager_response = client.get_secret_value(SecretId=SECRET_ID)
    secret_string = json.loads(secretsmanager_response["SecretString"])
    return secret_string[slack_channel]


def post_to_channel(data):
    daily_headers = {"content-type": "application/json"}
    return requests.post(
        url=get_webhook_url(SLACK_CHANNEL),
        data=str({"text": data}),
        headers=daily_headers,
    )
