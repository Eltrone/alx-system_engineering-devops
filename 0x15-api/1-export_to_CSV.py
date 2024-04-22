#!/usr/bin/python3
""" Export data to CSV format """
import csv
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user_data = requests.get(f"{base_url}users/{user_id}").json()
    todo_data = requests.get(f"{base_url}todos", params={"userId": user_id}).json()

    username = user_data.get("username")
    csv_file = f"{user_id}.csv"

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            writer.writerow([user_id, username, task.get("completed"), task.get("title")])
