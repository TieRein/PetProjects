from botocore.vendored import requests


def get_xkcd(data):
    xkcd_response = requests.get(url=XKCD_URL)
    data = xkcd_response.json()
    return f"Comic Number: {str(data['num'])}\nTitle: {data['title']}\nAlt Text: {data['alt']}\n{data['img']}"


def get_calvin_and_hobbes():
    pass


def get(comic_name):
    if comic_name is "xkcd":
        return get_xkcd()
    elif comic_name is "calvin_and_hobbes":
        return get_calvin_and_hobbes()
