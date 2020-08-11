#!/usr/bin/python3

import sys; sys.path.append('/home/ubuntu/.local/lib/python3.6/site-packages/twilio/rest/')
from datetime import datetime
from threading import Timer
from twilio.rest import Client
import http.client
import json
import time
import data_config

reminder = "Yay! Your favorita barista works tomorrow!"
print(reminder)

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = data_config.account_sid
auth_token = data_config.auth_token
client = Client(account_sid, auth_token)

lisa = client.messages.create(
    body=reminder,
    from_='+14582255409',
    to=data_config.lisa_number
)

jacob = client.messages.create(
    body=reminder,
    from_='+14582255409',
    to=data_config.jacob_number
)

print(lisa.sid)
print(jacob.sid)
print("Done with python")
