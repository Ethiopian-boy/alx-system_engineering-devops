#!/usr/bin/python3
""" Export to CSV
extend your Python script to export data in the CSV format.
"""
import csv
import requests
from sys import argv

if __name__ = "__main__":
    """ Entry point """
    empId = argv[1]
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    url_user = 'https://jsonplaceholder.typicode.com/users'

    payload1 = {'userid': empId}
    payload2 = {'id': empId}

    req_todo = requests.get(url_todo, params=payload1)
    req_user = requests.get(url_user, params=payload2)

    total_tasks = req_todo.json()
    users = req_user.json()
    emp_name = users[0].get('username')

    with open('{}.csv'.format(empId), mode='w') as user_file:
        write_file = csv.writer(user_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)
        for task in total_tasks:
            write_file.writerow(["{}".format(empId), "{}".format(
                emp_name), "{}".format(task.get(
                        'completed')), "{}".format(task.get('title'))])
