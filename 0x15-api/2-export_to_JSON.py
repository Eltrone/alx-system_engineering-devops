#!/usr/bin/python3
""" script to export data in the JSON format """
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_url = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user_url.get("username")
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.json".format(user_id), "w", newline="") as f:
        json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
            } for t in todo]}, f)
