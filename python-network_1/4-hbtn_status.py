#!/usr/bin/python3
"""
Module that fetches https://alu-intranet.hbtn.io/status or a given URL
using the requests package.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    if len(sys.argv) > 1:
        url = sys.argv[1]
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
