#!/bin/bash
#sends a request to URL passed as argument
curl -sw "%{http-code}" -o /dev/null
