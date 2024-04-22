#!/usr/bin/python3
""" Script using a REST API, for given employee ID """

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)
        user_data = user_response.json()
        todo_data = todo_response.json()

        employee_name = user_data.get('name')
        total_tasks = len(todo_data)
        done_tasks = [task for task in todo_data if task.get('completed')]
        total_done_tasks = len(done_tasks)

        print("Employee {} is done with tasks ({} / {}):".format(employee_name, total_done_tasks, total_tasks))
        for task in done_tasks:
            print(f"\t{task.get('title')}")
    except Exception as e:
        print(f"An error occurred: {e}")
