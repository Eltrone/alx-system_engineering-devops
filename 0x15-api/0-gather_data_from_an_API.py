#!/usr/bin/python3
""" script to export data in the JSON format """
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_url = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as f:
        json.dump({
            a.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": a.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": a.get("id")}).json()]
            for a in user_url}, f)
