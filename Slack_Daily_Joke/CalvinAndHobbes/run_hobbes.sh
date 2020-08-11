#!/bin/bash

echo "Above"

/usr/bin/node /home/ubuntu/PetProjects/Slack_Daily_Joke/CalvinAndHobbes/getURL.js > /home/ubuntu/PetProjects/Slack_Daily_Joke/CalvinAndHobbes/node.log

echo "Middle"

/usr/bin/python3 /home/ubuntu/PetProjects/Slack_Daily_Joke/CalvinAndHobbes/hobbes_comic.py > /home/ubuntu/PetProjects/Slack_Daily_Joke/CalvinAndHobbes/python3.log

echo "Below"
