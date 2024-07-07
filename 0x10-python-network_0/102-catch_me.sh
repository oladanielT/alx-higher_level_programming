#!/bin/bash
#Bash script to make a request
curl -sL -X PUT "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
