#!/usr/bin/python3
"""
Takes in a url and email and sends a POST request to the passed url
"""


import urllib.parse
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    myData = urllib.parse.urlencode({'email': email}).encode('ascii')
    with urllib.request.urlopen(url, data=myData) as response:
        print(response.read().decode('UTF8-8'))
