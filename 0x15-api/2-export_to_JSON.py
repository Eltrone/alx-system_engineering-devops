#!/usr/bin/python3
""" Script to export data in the JSON format """
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_url = requests.get(url + "users/{}".format(user_id)).json()
    username = user_url.get("username")
    todo = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as f:
        json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
            } for t in todo]}, f)
