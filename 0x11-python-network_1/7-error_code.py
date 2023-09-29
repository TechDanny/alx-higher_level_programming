#!/usr/bin/python3
"""
Takes in url, sends a request to the url and displays the body of the response
"""


from sys import argv[1]
import requests


if __name__ == "__main__":
    url = argv[1]
    response = requests,get(url)
    if response.status_code < 400:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))
