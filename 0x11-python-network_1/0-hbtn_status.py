#!/usr/bin/python3
"""Function to fetch from a url"""
import urllib.request
url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as res:
    req = res.read()
    print('Body response:')
    print('\t- type: ', type(req))
    print('\t- content: ', req)
    print('\t- utf8 content: ', req.decode('utf-8'))
