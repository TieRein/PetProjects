import requests
import data_config

dad_url = "https://icanhazdadjoke.com"
dad_headers = { 'accept': "application/json" }
dad_r = requests.get(url = dad_url, headers = dad_headers)
data = dad_r.json()

push = { "text": data['joke'] }

daily_headers = { "content-type": "application/json" }
slack_r = requests.post(url = data_config.daily_url, data = str(push), headers = daily_headers)

print(slack_r.text)
