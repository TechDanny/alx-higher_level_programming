#!/usr/bin/python3
"""
Takes two arguments
"""


from sys import argv
import requests


if __name__ == "__main__":
    repo_name = argv[1]
    owner_name = argv[2]
    url = requests.get("https://api.github.com/repos/{}/{}/commits".format(
                       owner_name, repo_name))
    r_file = url.json()
    try:
        for n in range(10):
            print(r_file[n].get('sha'), r_file[i].get('commit').get(
                  'author').get('name'), sep=": ")
    except:
        pass
