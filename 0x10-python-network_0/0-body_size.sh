#!/usr/bin/env bash

if [ $# -ne 1 ]; then
	exit 1
fi

URL=$1

SIZE=$(curl -s "$URL" | wc -c)

echo "$SIZE"
