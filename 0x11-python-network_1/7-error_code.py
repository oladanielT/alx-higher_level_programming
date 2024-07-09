#!/usr/bin/python3
"""
 Python script that takes in a URL, sends a request to the URL
 and displays the body of the response
"""
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    status = response.status_code
    print((response.text) if status < 400 else "Error code: {}".format(status))
