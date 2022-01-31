#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""
if __name__ == "__main__":
    import urllib.request as ureq
    import requests
    import sys
    import json

    args = sys.argv

    def find_user():
        with ureq.urlopen('https://jsonplaceholder.typicode.com/users') as f:
            list_users = json.load(f)
            for user in list_users:
                if user["id"] == int(args[1]):
                    return user

    def find_todo():
        response = requests.get('https://jsonplaceholder.typicode.com/todos')
        list_todo = response.json()
        todos = []
        total_todos = 0
        for todo in list_todo:
            if todo['userId'] == int(args[1]):
                total_todos += 1
            if todo['userId'] == int(args[1]) and todo['completed'] is True:
                todos.append(todo["title"])
        return todos, total_todos

    def user_todo():
        user_found = find_user()
        todo_found = find_todo()
        leni = len(todo_found[0])
        print(f'Employee {user_found["name"]} is done with tasks\
              ({leni}/{todo_found[1]}):')
        for x in range(leni):
            print(f'\t {todo_found[0][x]}')

    user_todo()
