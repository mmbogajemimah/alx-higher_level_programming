#!/usr/bin/python3
"""
A script that takes in a URL and an Email
Sends a post request to the passed URL with the email as a parameter
Displays the body of the response
"""


import requests
from sys import argv

if __name__ == '__main__':

    url = argv[1]
    parameters = {"email": argv[2]}
    r = requests.post(url, data=parameters)
    print(r.text)
