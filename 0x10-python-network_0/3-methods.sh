#!/bin/bash
# Bash script to  display all HTTP methods the server will accept
curl -s -I "$1" | grep "Allow" | cut -d " " -f2-
