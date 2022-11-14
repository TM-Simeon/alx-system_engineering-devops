#!/usr/bin/python3
"""script to get information about an employee using rest api"""
import requests
import sys
if __name__ == '__main__':
    """only run code when ran as main"""
    userId = sys.argv[1]
    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'"
    ".format(userId))
    name = response.json().get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    notCompleted = 0
    completed = 0
    for todo in todos.json():
        if todo.json().get('userId') == int(userId):
            if todo.json().get('completed'):
                completed += 1
            else:
                notCompleted += 1
    print('Employee {} is done with tasks({}/{}):\n'.format(name,"
    "completed,(completed + notCompleted)))
    for todo in todos.json():
        if todo.json().get('userId') == int(userid) and "
        "todo.json().get('completed'):
            print('\t\s{}'.format(todos.json().get('title')))
