#!/usr/bin/python3
"""A script that
- a Python script that takes in a URL,
    sends a request to the URL and
    displays the body of the response (decoded in utf-8).
"""
if __name__ == '__main__':
    import requests
    import sys
    url = sys.argv[1]
    res = requests.get(url)
    if res.status_code < 400:
        print(res.text)
    else:
        print("Error code: {}".format(res.status_code))
