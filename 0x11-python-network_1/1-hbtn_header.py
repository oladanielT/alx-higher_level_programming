#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""

import sys
import urllib.request
if __name__ == "__main__":
    """Shouldn't run if imported"""
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        headers = dict(response.headers)
        print("{}".format(headers['X-Request-Id']))
