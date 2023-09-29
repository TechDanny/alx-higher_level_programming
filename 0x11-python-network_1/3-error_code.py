#!/usr/bin/python3
"""
Takes a url and sends a request to the url
"""


from sys import argv
from urllib import error
from urllib import request


if __name__ == "__main__":
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            myUrl = response.read()
            print(myUrl.decode('UTF-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
