#!/usr/bin/python3
"""
Script using a REST API, for given employee ID
"""

import csv
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(base_url + "users/{}".format(sys.argv[1])).json()
    todo_data = requests.get(base_url + "todos",
                             params={"userId": sys.argv[1]}).json()

    user_id = user_data.get("id")
    username = user_data.get("username")

    csv_file = f"{user_id}.csv"

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

    print(f"Data exported to {csv_file}")
