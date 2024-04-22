#!/usr/bin/python3
""" Script to fetch tasks of all employees and export them to a JSON file """

import json
import requests

def fetch_all_data():
    """ Fetches data of all users and their tasks using the REST API """
    base_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(base_url + "users").json()
    todos = requests.get(base_url + "todos").json()

    user_dict = {user['id']: user['username'] for user in users}
    tasks_dict = {user_id: [] for user_id in user_dict.keys()}

    for todo in todos:
        task_info = {
            "username": user_dict[todo["userId"]],
            "task": todo["title"],
            "completed": todo["completed"]
        }
        tasks_dict[todo["userId"]].append(task_info)

    return tasks_dict

def export_all_to_json():
    """ Exports all tasks of all employees to a JSON file """
    tasks_dict = fetch_all_data()
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(tasks_dict, jsonfile)

if __name__ == "__main__":
    export_all_to_json()
