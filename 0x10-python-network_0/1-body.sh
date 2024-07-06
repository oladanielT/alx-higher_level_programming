#!/bin/bash
# Check if a URL is provided
[ -z "$1" ] && exit 1  # Exit if no URL is provided

# Send GET request to the URL and display the body of the response
curl -sfL "$1"
