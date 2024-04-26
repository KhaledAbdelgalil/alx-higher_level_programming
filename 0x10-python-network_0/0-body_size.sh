#!/bin/bash
# Script that takes in a URL then sends a request, and displays the size of the body of the response
curl -s "$1" | wc -c
