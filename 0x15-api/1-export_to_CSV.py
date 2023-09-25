#!/usr/bin/python3
"""Script that accesses REST API for employee todo list"""

import requests
import sys


if __name__ == '__main__':
    employee_Id = sys.argv[1]
    base_Url = "https://jsonplaceholder.typicode.com/users"
    url = base_Url + "/" + employee_Id

    response = requests.get(url)
    username = response.json().get('username')

    todo_Url = url + "/todos"
    response = requests.get(todo_Url)
    tasks = response.json()

    with open('{}.csv'.format(employee_Id), 'w') as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'
                    .format(employee_Id, username, task.get('completed'),
                            task.get('title')))
