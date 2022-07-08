import requests
import data_config

dilbert_r = requests.get(url = data_config.dilbert_url)
data = dilbert_r.json()
output = "Title: " + str(data['title']) + "\nhttps:" + data['image']
print(output)

memory = open('/home/ubuntu/PetProjects/Slack_Daily_Joke/dilbert_last.txt', 'r')
last_comic = memory.read()
memory.close()

push = { "text": output }

daily_headers = { "content-type": "application/json" }

if last_comic != output:
    slack_r = requests.post(url = data_config.daily_url, data = str(push), headers = daily_headers)
    memory = open('/home/ubuntu/PetProjects/Slack_Daily_Joke/dilbert_last.txt', 'w')
    memory.write(output)
    memory.close()
    
