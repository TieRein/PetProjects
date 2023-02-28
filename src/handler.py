import logging
import metadata
import slack
import comic

logger = logging.getLogger()


def lambda_handler(event, context):
    comic_name = event["comic_name"]
    comic_data = comic.get(comic_name)
    logger.info(f"Output: {comic_data}")

    if metadata.get(comic_name) == comic_data:
        return "no new comic"
    
    # send to slack
    slack_response = slack.post_to_slack(comic_data)
    if slack_response.status_code != 200:
        logger.error("Unable to post to Slack")
        slack_response.raise_for_status()

    # save metadata
    metadata.save(comic_name, comic_data)
    return f"Published comic. Slack response: {slack_response.status_code}"
