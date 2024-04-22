#!/usr/bin/python3
""" Script using a REST API, for given employee ID """

import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(base_url + "users/{}".format(sys.argv[1])).json()
    todo_data = requests.get(base_url + "todos", params={"userId": sys.argv[1]}).json()

    completed_tasks = [task.get("title") for task in todo_data if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get("name"), len(completed_tasks), len(todo_data)))
    [print("\t{}".format(task)) for task in completed_tasks]
