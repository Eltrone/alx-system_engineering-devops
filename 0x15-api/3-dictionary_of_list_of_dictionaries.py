#!/usr/bin/python3
import json
import requests

def fetch_all_data():
    """ Récupère les données de tous les utilisateurs et de toutes leurs tâches via l'API """
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

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
    """ Exporte les données de toutes les tâches de tous les employés au format JSON """
    tasks_dict = fetch_all_data()
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(tasks_dict, jsonfile)

if __name__ == "__main__":
    export_all_to_json()

