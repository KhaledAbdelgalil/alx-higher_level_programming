#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io headers
"""
if __name__ == '__main__':
    from urllib import request
    import sys

    req = request.Request(sys.argv[1])
    with request.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
