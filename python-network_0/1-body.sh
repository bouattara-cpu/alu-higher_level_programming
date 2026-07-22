#!/bin/bash
# Takes in a URL, sends a GET request, and displays the body of a 200 response
curl -s -L "$1"
