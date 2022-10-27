#!/usr/bin/python3
"""
A script that takes in a URL and an Email
Sends a post request to the passed URL with the email as a parameter
Displays the body of the response
"""


import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    parameter = {"email": argv[2]}
    data = urllib.parse.urlencode(parameter).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as resp:
        print(resp.read().decode("utf-8"))
