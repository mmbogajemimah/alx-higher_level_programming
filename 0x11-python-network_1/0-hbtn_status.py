#!/usr/bin/python3
"""
This Script: fetches https://alx-intranet.hbtn.io/status
Then displays the body
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        information = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(information)))
        print("\t- content: {}".format(information))
        print("\t utf8 content: {}".format(information.decode('utf-8')))
