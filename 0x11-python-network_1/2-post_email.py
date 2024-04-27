#!/usr/bin/python3
"""A script that
- post an email to url.
"""
if __name__ == '__main__':
    from urllib import request
    from urllib import parse
    import sys
    url  = sys.argv[1]
    payload_dict = {"email": sys.argv[2]}
    payload_data = parse.urlencode(payload_dict).encode("ascii")
    with request.urlopen(request.Request(url, payload_data)) as res:
        print(res.read().decode("utf-8"))
    