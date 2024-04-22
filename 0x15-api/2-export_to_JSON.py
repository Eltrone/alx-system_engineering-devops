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
    user_response = requests.get(url + "users/{}".format(user_id))
    user_data = user_response.json()
    username = user_data.get("username")

    # Retrieve todo data for the user
    todo_response = requests.get(url + "todos", params={"userId": user_id})
    todo_data = todo_response.json()

    # Create dictionary to store JSON data
    json_data = {user_id: []}

    # Populate dictionary with todo data
    for task in todo_data:
        json_data[user_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    # Write data to JSON file
    with open("{}.json".format(user_id), "w") as json_file:
        json.dump(json_data, json_file)

    print("Data exported to {}.json".format(user_id))
