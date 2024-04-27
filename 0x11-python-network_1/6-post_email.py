#!/usr/bin/python3
"""A script that
- post an email to url.
"""
if __name__ == '__main__':
    import requests
    import sys
    url = sys.argv[1]
    payload_data = {"email": sys.argv[2]}
    res = requests.post(url, payload_data)
    print(res.text)
