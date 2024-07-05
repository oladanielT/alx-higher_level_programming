#!/bin/bash
# script to get the body size of a request
curl -s $1 | wc -c

