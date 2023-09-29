#!/usr/bin/python3
"""
Takes a url and sends a request to the url
"""


from sys import argv
from urllib import parse
from urllib import request


if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            myUrl = response.read()
            print(myUrl.decode('UTF-8'))
    except urllib.erro.HTTPError as e:
        print("Error code: {}".format(e.code))
