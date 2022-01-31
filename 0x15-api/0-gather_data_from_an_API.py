#!/usr/bin/python3
""" JSon API """


if __name__ == "__main__":
    import requests
    from sys import argv

    def find_user():
        """ find the user """
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        list_users = response.json()

        for user in list_users:
            if user["id"] == int(argv[1]):
                return user

    def find_todo():
        """ find todos """
        todos = []
        total_todos = 0
        response = requests.get('https://jsonplaceholder.typicode.com/todos')
        list_todo = response.json()

        for todo in list_todo:
            if todo['userId'] == int(argv[1]):
                total_todos += 1
            if todo['userId'] == int(argv[1]) and todo['completed'] is True:
                todos.append(todo["title"])
        return todos, total_todos

    def user_todo():
        """ display funcs """
        leni = 0

        user_found = find_user()
        todo_found = find_todo()
        leni = len(todo_found[0])

        print('Employee {} is done with tasks({}/{}):'.
              format(user_found["name"], leni, todo_found[1]))

        for x in range(leni):
            print('\t {}'.format(todo_found[0][x]))

    user_todo()
