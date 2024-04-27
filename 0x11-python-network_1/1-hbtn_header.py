#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
"""
if __name__ == '__main__':
    from urllib import request
    import sys

    with request.urlopen(sys.argv[1]) as res:
        print(dict(res.headers)["X-Request-Id"])
