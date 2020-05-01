import requests
import data_config

xkcd_r = requests.get(url = data_config.xkcd_url)
data = xkcd_r.json()
output = "Comic Number: " + str(data['num']) + "\nTitle: " + data['title'] + "\nAlt Text: " + data['alt'] + "\n" + data['img']
print(output)

memory = open('/home/ubuntu/PetProjects/Discord_Daily_Joke/xkcd_last.txt', 'r')
last_comic = memory.read()
memory.close()

push = {
    "username": "Daily XKCD",
    "avatar_url": "https://i.imgur.com/4M34hi2.png",
    "content": output
    }

if last_comic != output:
    #discord_r = requests.post(url = data_config.daily_url, data = push)
    discord_r = requests.post(url = data_config.avoaus_url, data = push)
    memory = open('/home/ubuntu/PetProjects/Discord_Daily_Joke/xkcd_last.txt', 'w')
    memory.write(output)
    memory.close()
