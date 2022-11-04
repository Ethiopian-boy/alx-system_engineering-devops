#!/usr/bin/python3
""" Dictionary of list of dictionaries """
import json
import requests

if __name__ == "__main__":
    """ Entry point """
    empId = 1
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    url_user = 'https://jsonplaceholder.typicode.com/users'

    total_users = requests.get(url_user).json()
    user_tasks = {}

    for empId in range(1, len(total_users) + 1):
        req_todo = requests.get(url_todo, params={'userId': empId})
        req_user = requests.get(url_user, params={'id': empId})

        total_tasks = req_todo.json()
        users = req_user.json()

        list_dict = []
        emp_name = users[0].get('username')

        for task in total_tasks:
            task_info = {}
            task_info['task'] = task.get('title')
            task_info['completed'] = task.get('completed')
            task_info['username'] = emp_name
            list_dict.append(task_info)
        user_tasks[empId] = list_dict

    with open('todo_all_employees.json', 'w') as json_file:
        info = josn.dumps(user_tasks)
        json_file.write(info)
