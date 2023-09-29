#!/usr/bin/python3
"""
fetching https://alx-intranet.hbtn.io/status
"""


from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        html_response = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html_response)))
        print("\t- content: {}".format(html_response))
        print("\t- utf8 content: {}".format(html_response.decode('utf-8')))
