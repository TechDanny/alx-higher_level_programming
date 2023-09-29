#!/usr/bin/python3
"""
Takes in a url and email address, sends a POST request to the url with email
and displays the body of the response
"""


from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
