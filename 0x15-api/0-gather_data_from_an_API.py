#!/usr/bin/python3

import requests
import sys

if __name == "__main__":
    #define rest url
    url = "https://jsonplaceholder.typicode.com/"
    #retrieve user info
    user_info = requests.get(url + "users/{}".format{sys.argv[1])).json()
    #retrive to do lists
    to_dos= requests.get(url + "todos", parms={userId": sys.argv[1]}).json()
    #
