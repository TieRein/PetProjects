import requests
import data_config

xkcd_r = requests.get(url = data_config.xkcd_url)
data = xkcd_r.json()
output = "Comic Number: " + str(data['num']) + "\nTitle: " + data['title'] + "\nAlt Text: " + data['alt'] + "\n" + data['img']
print(output)

memory = open('/home/ubuntu/PetProjects/Slack_Daily_Joke/xkcd_last.txt', 'r')
last_comic = memory.read()
memory.close()

push = { "text": output }

daily_headers = { "content-type": "application/json" }

if last_comic != output:
    slack_r = requests.post(url = data_config.daily_url, data = str(push), headers = daily_headers)
    memory = open('/home/ubuntu/PetProjects/Slack_Daily_Joke/xkcd_last.txt', 'w')
    memory.write(output)
    memory.close()
