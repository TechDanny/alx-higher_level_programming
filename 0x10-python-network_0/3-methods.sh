#!/bin/bash
#Takes in URL and displays all HTPP methods
curl -sIX OPTIONS "$1" | grep "Allow" | cut -d' ' -f 2-
