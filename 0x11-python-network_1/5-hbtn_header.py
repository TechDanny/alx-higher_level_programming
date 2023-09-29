#!/usr/bin/python3
"""
Takes in a url, sends a request to the url and displays the value
"""


from sys import argv
import requests


if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get("X-Request-Id"))
