#!/usr/bin/python3
""" JSon API """


if __name__ == "__main__":
    import json
    import requests
    import sys
    import urllib.request as ureq

    args = sys.argv

    def find_user():
        """ find the user """
        with ureq.urlopen('https://jsonplaceholder.typicode.com/users') as f:
            list_users = json.load(f)
            for user in list_users:
                if user["id"] == int(args[1]):
                    return user

    def find_todo():
        """ find todos """
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
        """ display funcs """
        user_found = find_user()
        todo_found = find_todo()
        leni = len(todo_found[0])
        print('Employee {} is done with tasks\
              ({}/{}):'.format(user_found["name"], leni, todo_found[1]))
        for x in range(leni):
            print(f'\t {todo_found[0][x]}')

    user_todo()
