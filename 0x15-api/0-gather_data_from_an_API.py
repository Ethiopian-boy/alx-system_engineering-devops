#!/usr/bin/python3
"""  a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress. """
import requests
from sys import argv

if __name__ == "__main__":
    """ Entry point """
    empId = argv[1]
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    url_user = 'https://jsonplaceholder.typicode.com/users'
    payload1 = {'userId': empId}
    payload2 = {'id': empId}

    req_todo = requests.get(url_todo, params=payload1)
    req_user = requests.get(url_user, params=payload2)

    total_tasks = req_todo.json()
    done_tasks = []
    for task in total_tasks:
        if (task.get('completed') is True):
            done_tasks.append(task)

    users = req_user.json()
    emp_name = users[0].get('name')

    print("Employee {:s} is done with task ({:d}/{:d}:".format(
        emp_name, len(done_tasks), len(total_tasks)))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
