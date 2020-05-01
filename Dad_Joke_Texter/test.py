#!/usr/bin/python3

from datetime import datetime
from threading import Timer
from twilio.rest import Client
import http.client
import json
import time

print("Start")
print("In function")
conn = http.client.HTTPSConnection("icanhazdadjoke.com")

headers = { 'accept': "application/json",
            'cache-control': "no-cache",
            'postman-token': "bad68f2f-309b-7215-8135-84fa741ccec4"
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
account_sid = 'AC73028952a69a527272a478f526d45766'
auth_token = '19d600317fc3a1dacb5519a3a945b669'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body=joke,
    from_='+14582255409',
    to='+13609520063'
)

print(message.sid)

