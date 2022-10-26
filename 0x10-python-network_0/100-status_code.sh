#!/bin/bash
# a Bash script that sends a request to a URL,displays only the status code of the response
curl -sI -o /dev/null -w "%{http_code}" "$1"
