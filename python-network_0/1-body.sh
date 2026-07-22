#!/bin/bash
# Sends a GET request to a URL and displays the body of a 200 status code response
curl -s -o /dev/stdout -w "%{http_code}" "$1"
