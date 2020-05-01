#!/usr/bin/python3

print("Start of python")

import sys; sys.path.append('/home/ubuntu/.local/lib/python3.6/site-packages/twilio/rest/')
from datetime import datetime
from threading import Timer
from twilio.rest import Client
import http.client
import json
import time
import data_config

print("Start of connection")
conn = http.client.HTTPSConnection("icanhazdadjoke.com")

headers = { 'accept': "application/json",
            'cache-control': "no-cache",
            'postman-token': data_config.postman_token
}
# sending get request and saving the response as response object 
conn.request("GET", "/", headers=headers)

# extracting data in json format 
res = conn.getresponse()
data = res.read() 
a_json = data.decode("utf-8")
b_json = json.loads(a_json)
joke = b_json["joke"]
print(joke)

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = data_config.account_sid
auth_token = data_config.auth_token
client = Client(account_sid, auth_token)

audrey = client.messages.create(
    body=joke,
    from_='+14582255409',
    to=data_config.audrey_number
)

theron = client.messages.create(
    body=joke,
    from_='+14582255409',
    to=data_config.theron_number
)

bridget = client.messages.create(
    body=joke,
    from_='+14582255409',
    to=data_config.bridget_number
)

seahorse = client.messages.create(
    body=joke,
    from_='+14582255409',
    to=data_config.seahorse_number
)

jacob = client.messages.create(
    body=joke,
    from_='+14582255409',
    to=data_config.jacob_number
)

cheezy = client.messages.create(
    body=joke,
    from_='+14582255409',
    to=data_config.cheezy_number
)

mel = client.messages.create(
    body=joke,
    from_='+14582255409',
    to=data_config.mel_number
)

devon = client.messages.create(
    body=joke,
    from_='+14582255409',
    to=data_config.devon_number
)

mel_friend = client.messages.create(
    body=joke,
    from_='+14582255409',
    to=data_config.mel_friend_number
)

print(audrey.sid)
print(theron.sid)
print(bridget.sid)
print(seahorse.sid)
print(jacob.sid)
print(cheezy.sid)
print(mel.sid)
print(devon.sid)
print(mel_friend.sid)
print("Done with python")
