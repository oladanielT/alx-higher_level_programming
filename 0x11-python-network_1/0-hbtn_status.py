#!/usr/bin/python3
"""
function to fetch from
https://alx-intranet.hbtn.io/status
"""


import urllib.request


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
    body = res.read()
    print("Body response:")
    print("\t- type: ", type(body))
    print("\t- content: ", body)
    print("\t- utf8 content: ", body.decode('utf-8'))
