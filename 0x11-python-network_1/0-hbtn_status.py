#!/usr/bin/python3
"""Function to fetch from a url"""
import urllib.request


url = 'https://alx-intranet.hbtn.io/status'
try:
    with urllib.request.urlopen(url) as req:
        response = req.read()
        print("Body response:")
        print("\t- type: ", type(response))
        print("\t- content: ", response)
        print("\t- utf8: ", response.decode('utf-8'))
except urllib.error.Urlerror as er:
    print(er.reason)
