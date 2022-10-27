#!/usr/bin/python3
"""
This script takes in a URL and sends a request to the URL
then Displays the body of the response decoded in utf-8
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    url = argv[1]
    resp = requests.get(url)
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
