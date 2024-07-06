#!/bin/bash
#Bash script to send request and display status code
curl -s -0 /dev/null -w "%{http_code}" "$1"
