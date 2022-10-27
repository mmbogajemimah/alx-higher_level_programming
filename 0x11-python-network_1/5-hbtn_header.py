#!/usr/bin/python3
"""
This script: Takes in a URL, Sends a request to the URL,
displays the value of the X-Request-Id found in the header
"""


from sys import argv
import requests

if __name__ == '__main__':
    url = argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
