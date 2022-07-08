#!/usr/bin/python3

import sys; sys.path.append('/home/ubuntu/.local/lib/python3.6/site-packages/twilio/rest/')
import datetime
import requests
import data_config

now = datetime.datetime.now()
date_compare = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
output = "Calvin and Hobbes"
date = ""
with open("hobbes.txt") as f:
    line = f.readline()
    count = 0
    while line:
        if count == 0:
            line = line.rstrip("\n")
            date = line
            line = str(now.day) + "/" + now.strftime("%B") + "/" + str(now.year)
            count += 1
        output += "\n" + line
        line = f.readline()


print("Output: \n" + output)
print("\nDate: " + date)


push = { "text": output }

daily_headers = { "content-type": "application/json" }

if date == date_compare:
    slack_r = requests.post(url = data_config.daily_smile, data = str(push), headers = daily_headers)
