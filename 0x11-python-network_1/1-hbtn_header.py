#!/usr/bin/python3
"""
Takes in a URL sends a request to the url and displays the value
"""


import sys
from urllib import request


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        x = response.info()
        print(x.get('X-Request-Id'))
