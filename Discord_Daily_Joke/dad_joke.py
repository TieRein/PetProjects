import requests
import data_config

dad_url = "https://icanhazdadjoke.com"
dad_headers = { 'accept': "application/json" }
dad_r = requests.get(url = dad_url, headers = dad_headers)
data = dad_r.json()

push = {
    "username": "Daily Dad Joke",
    "avatar_url": "https://i.imgur.com/4M34hi2.png",
    "content": data['joke']
    }

discord_r = requests.post(url = data_config.daily_url, data = push)
#discord_r = requests.post(url = data_config.avoaus_url, data = push)
