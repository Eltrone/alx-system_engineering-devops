#!/usr/bin/python3
""" Script using a REST API, for given employee ID """

import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(base_url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(base_url + "todos", params={"userId": sys.argv[1]}).json()

    comp = [t.get("title") for t in todo if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get("name"), len(comp), len(todo)))
    [print("\t {}".format(c)) for c in comp]
