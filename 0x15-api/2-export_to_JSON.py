#!/usr/bin/python3
""" Export data to JSON format """
import json
import requests
import sys

if __name__ == "__main__":
    # Extract user ID from command line argument
    user_id = sys.argv[1]
    # Base URL for the API
    url = "https://jsonplaceholder.typicode.com/"
    # Retrieve user data
    user_url = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user_url.get("username")
    # Retrieve todo data for the user
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.json".format(user_id), "w", newline="") as f:
        json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
            } for t in todo]}, f)
