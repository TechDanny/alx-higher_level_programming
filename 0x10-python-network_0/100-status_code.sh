#!/bin/bash
#sends a request to URL passed as argument
curl -sw "%{http_code}" -o /dev/null
