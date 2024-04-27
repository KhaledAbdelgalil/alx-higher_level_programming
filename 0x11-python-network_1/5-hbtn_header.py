#!/usr/bin/python3
"""
Python script that fetches an URL
"""


if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))
