#!/bin/bash
# script displays only the status code of the response
curl -s "$1" -o ./tmp.txt -w "%{http_code}"
