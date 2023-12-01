#!/usr/bin/python3
"""A script that takes in a letter and sends a POST request to n-webpage
with the letter as a parameter."""
import sys, requests

if __name__ == '__main__':

    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}
    req = requests.post(url, data=payload)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
        