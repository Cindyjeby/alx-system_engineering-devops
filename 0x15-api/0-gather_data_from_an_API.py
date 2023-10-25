#!/usr/bin/python3
"""get data from an API"""

import requests
import sys


if __name__ == "__main__":
    #define rest url
    url = "https://jsonplaceholder.typicode.com/"

    #retrieve user info
    user = requests.get(url + "users/{}".format{sys.argv[1])).json()

    #retrive to do lists
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    #
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    #print employee name
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    #print title
    [print("\t {}".format(c)) for c in completed]
