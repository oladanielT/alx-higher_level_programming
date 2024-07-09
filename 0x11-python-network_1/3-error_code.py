#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import sys
import urllib
import urllib.request

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print("{}".format(body))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(error.reason))
