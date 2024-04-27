#!/usr/bin/python3
"""A script that:
- list 10 recent commits for github repo
"""


if __name__ == "__main__":
    import sys
    import requests
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    response = requests.get(url)
    for i in range(10):
        try:
            print(response.json()[i].get("sha"), end=": ")
            print(response.json()[i].get("commit").get("author").get("name"))
        except IndexError:
            pass
