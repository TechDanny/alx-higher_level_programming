#!/bin/bash
#Takes in URL and displays all HTPP methods
curl -Is "$1" | grep Allow | cut -c 8-
