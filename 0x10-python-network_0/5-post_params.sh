#!/bin/bash
#Bash to send a POST request to the server
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
