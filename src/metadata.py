import logging
import boto3


TABLE_NAME = "nike_daily_smile_tracking"
TABLE = boto3.resource("dynamodb").Table(TABLE_NAME)


def get(comic_name):
    db_entry_key = {"comic_name": comic_name}
    db_item = TABLE.get_item(Key=db_entry_key)
    if not db_item.get("Item") or not db_item["Item"].get("output"):
        return None
    return db_item["Item"]["output"]


def save(comic_name, output):
    db_entry = {"comic_name": comic_name, "output": output}
    TABLE.put_item(Item=db_entry)
