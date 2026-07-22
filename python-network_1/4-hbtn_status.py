#!/usr/bin/python3
"""
Module that fetches a given URL using the requests package
and displays response details.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
