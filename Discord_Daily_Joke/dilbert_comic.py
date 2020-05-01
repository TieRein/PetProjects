import requests
import data_config

dilbert_r = requests.get(url = data_config.dilbert_url)
data = dilbert_r.json()
output = "Title: " + str(data['title']) + "\nhttps:" + data['image']
print(output)

memory = open('/home/ubuntu/PetProjects/Discord_Daily_Joke/dilbert_last.txt', 'r')
last_comic = memory.read()
memory.close()

push = {
    "username": "Daily Dilbert",
    "avatar_url": "https://i.imgur.com/4M34hi2.png",
    "content": output
    }

if last_comic != output:
    #discord_r = requests.post(url = data_config.daily_url, data = push)
    discord_r = requests.post(url = data_config.avoaus_url, data = push)
    memory = open('/home/ubuntu/PetProjects/Discord_Daily_Joke/dilbert_last.txt', 'w')
    memory.write(output)
    memory.close()
