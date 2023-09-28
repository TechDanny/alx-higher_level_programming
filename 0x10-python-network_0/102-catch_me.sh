#!/bin/bash
#makes a request
curl -sLX PUT -H "Origin: HolbertonSchool" -d "user_d=98" 0.0.0.0:5000/catch_me
