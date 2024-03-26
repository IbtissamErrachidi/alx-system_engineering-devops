#!/usr/bin/python3
"""
Exports to-do list information of all employees to JSON format.
"""

import json
import requests


def fetch_user_data():
    """Fetch user information and to-do lists for all employees."""
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()
    with open("todo_all_employees.json", "w") as jsonfile:
        all_tasks = {}
        for user in users:
            user_id = user.get("id")
            tasks = requests.get(url + "todos", params={"userId": user_id}).json()
            user_tasks = [{
                "userId": user_id,  # Ajout du champ userId
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            } for task in tasks]
            all_tasks[user_id] = user_tasks
