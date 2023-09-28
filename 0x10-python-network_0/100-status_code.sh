#!/bin/bash
#sends a request to URL passed as argument
curl -sw "%{http_code}" "$1" -o /dev/null
