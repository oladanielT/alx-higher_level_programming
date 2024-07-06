#!/bin/bash
#Bash script to display the HTTP methods to allow.
curl -sI "$1" | grep "Allow" | cut -d " " -f2
