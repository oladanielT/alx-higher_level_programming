#!/usr/bin/python3
"""
Python script to fetch from
https://alx-intranet.hbtn.io/status
"""
import urllib.request
with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    body_mess = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body_mess)))
    print("\t- content: {}".format(body_mess))
    print("\t- utf8 content: {}".format(body_mess.decode('utf-8')))
