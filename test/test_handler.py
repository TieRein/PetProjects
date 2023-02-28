import handler

def test_handler_should_save_metadata_when_slack_responds_200(mocker):
    event = {"comic_name": "random_comic_name"}
    response = handler.lambda_handler(event, [])