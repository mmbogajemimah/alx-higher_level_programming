#!/bin/bash
#  a Bash script that sends a JSON POST request to a URL passed
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
