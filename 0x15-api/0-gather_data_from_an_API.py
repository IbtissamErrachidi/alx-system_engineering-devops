#!/usr/bin/python3
"""
Retourne les informations de la liste de tâches pour un ID d'employé donné.
"""

import requests
import sys


if __name__ == "__main__":
    # URL de base pour l'API JSONPlaceholder
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(employee_id)).json()

    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(name, todos_done, todos_count).strip())

    [print("\t {}".format(complete)) for complete in completed]

