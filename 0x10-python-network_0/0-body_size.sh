#!/bin/bash
# takes a URL and sends request to that URL

curl -s "$1" | wc -c
