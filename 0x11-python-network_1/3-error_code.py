#!/usr/bin/python3
"""
This script takes in a URL and sends a request to the URL
hen Displays the body of the response decoded in utf-8
"""


if __name__ == "__main__":
    from sys import argv
    from urllib import request, error

    url = argv[1]
    try:
        with request.urlopen(url) as resp:
            print(resp.read().decode("utf-8"))
    except error.HTTPError as e:
        print('Error code:', e.code)
