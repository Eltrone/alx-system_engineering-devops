#!/usr/bin/python3
""" Export data to JSON format """
import json
import requests
import sys

if __name__ == "__main__":
    # Base URL for the API
    url = "https://jsonplaceholder.typicode.com/"

    # Extract user ID from command line argument
    user_id = sys.argv[1]

    # Retrieve user data
    user_response = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user_response.get("username")

    # Retrieve todo data for the user
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.json".format(user_id), "w", newline="") as f:
        json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
            } for t in todo]}, f)
