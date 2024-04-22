#!/usr/bin/python3
""" Gather_data_from_an_API """
import sys
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_url = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    comp = [t.get("title") for t in todo if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_url.get("name"), len(comp), len(todo)))
    [print("\t {}".format(c)) for c in comp]
