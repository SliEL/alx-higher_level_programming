#!/usr/bin/python3
"""A script that fetches a url."""
import requests

if __name__ == '__main__':

    url = "https://intranet.hbtn.io/status"
    req = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
