#!/bin/bash
# Bash script that makes a request, causes the server to respond with a message
curl -sX PUT -L -d "user_id=98" --header "origin: HolbertonSchool" 0.0.0.0:5000/catch_me
