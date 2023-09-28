#!/bin/bash
#sends JSON POST request to a URL passed as first argument
curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2"
