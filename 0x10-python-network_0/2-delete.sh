#!/bin/bash
# Bash script sends DELETE request to URL and displays body of response
curl -s "$1" -X DELETE
