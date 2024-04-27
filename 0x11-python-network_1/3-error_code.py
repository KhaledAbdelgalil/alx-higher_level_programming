#!/usr/bin/python3
"""A script that
- a Python script that takes in a URL,
    sends a request to the URL and
    displays the body of the response (decoded in utf-8).
"""
if __name__ == '__main__':
    from urllib import request
    from urllib import error
    import sys
    url = sys.argv[1]
    try:
        with request.urlopen(url) as res:
            print(res.read().decode("utf-8"))
    except error.HTTPError as err:
        print('Error code:', err.code)
