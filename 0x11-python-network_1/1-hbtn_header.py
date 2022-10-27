#!/usr/bin/python3
"""
This script: Takes in a URL, Sends a request to the URL,
displays the value of the X-Request-Id found in the header
"""


from sys import argv
import urllib.request

if __name__ == '__main__':
    url = argv[1]
    with urllib.request.urlopen(url) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
