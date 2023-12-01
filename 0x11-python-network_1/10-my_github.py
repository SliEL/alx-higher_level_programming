#!/usr/bin/python3
"""A script that takes your Github credentials (username and password)
and uses the Github API to display your id"""
import sys, requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':

    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get(url, auth=auth)
    print(req.json().get('id'))
