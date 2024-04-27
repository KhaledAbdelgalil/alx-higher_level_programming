#!/usr/bin/python3
"""A script that
- a Python script tthat takes in a letter
 sends a POST request to http://0.0.0.0:5000/search_user with
 the letter as a parameter.
"""
if __name__ == '__main__':
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    q = ""
    if len(sys.argv) >= 2:
        q = sys.argv[1]
    payload_data = {"q": q}

    res = requests.post(url, data=payload_data)
    try:
        res_json = res.json()
        if res_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(res_json.get("id"), res_json.get("name")))
    except ValueError:
        print("Not a valid JSON")
