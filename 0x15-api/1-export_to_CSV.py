#!/usr/bin/python3
""" Export data to CSV format """
import csv
import requests
import sys

if __name__ == "__main__":
    # Base URL for the API
    baseurl = "https://jsonplaceholder.typicode.com/"

    # Extract user ID from command line argument
    user_id = sys.argv[1]

    # Retrieve user data
    user_response = requests.get(baseeurl + "users/{}".format(user_id))
    user_data = user_response.json()
    username = user_data.get("username")

    # Retrieve todo data for the user
    todo_response = requests.get(baseurl + "todos", params={"userId": user_id})
    todo_data = todo_response.json()

    # Write data to CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo_data:
            csv_writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
