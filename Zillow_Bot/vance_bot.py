import requests
import config

daily_headers = {"content-type": "application/json"}
vance_r = requests.get(url=config.vance_url, headers=config.headers)
current_count = vance_r.text.split("<title>Single Family Homes For Sale - ")[1].split(" Homes | Zillow</title>")[0]

notification = "Hey Vance, a new house was posted!"

memory = open('./vance_last.txt', 'r')
last_count = memory.read()
memory.close()

push = {"text": notification}


print("last_count", last_count)
print("current_count", current_count)

if last_count < current_count:
    print("Notification sent")
    slack_r = requests.post(url=config.zillow_bot_url, data=str(push), headers=daily_headers)

memory = open('./vance_last.txt', 'w')
memory.write(current_count)
memory.close()
