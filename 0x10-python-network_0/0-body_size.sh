#!/bin/bash
# takes a URL and sends request to that URL

curl -sI "$1" | wc -c
