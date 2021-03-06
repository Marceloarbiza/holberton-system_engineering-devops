#!/usr/bin/python3
""" JSon API """


if __name__ == "__main__":
    import csv
    import json
    import requests
    from sys import argv

    def find_user(n):
        """ find the user """
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        list_users = response.json()

        for user in list_users:
            if user["id"] == int(n):
                return user

    def find_todo(n):
        """ find todos """
        todos_true = []
        todos_totales = []
        count_totales = 0
        response = requests.get('https://jsonplaceholder.typicode.com/todos')
        list_todo = response.json()

        for todo in list_todo:
            if todo['userId'] == int(n):
                todos_totales.append(todo)
                count_totales += 1
            if todo['userId'] == int(n) and todo['completed'] is True:
                todos_true.append(todo)
        return todos_true, count_totales, todos_totales

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

    def to_csv():
        """ export to CSV """
        user_found = find_user()
        todo_found = find_todo()
        file_csv = '{}.csv'.format(argv[1])

        u_id = user_found["id"]
        u_username = user_found["username"]

        li_user = [u_id, u_username, '', '']

        with open(file_csv, 'w') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for t in todo_found[2]:
                li_user[2] = t["completed"]
                li_user[3] = t["title"]
                writer.writerow(li_user)

    def to_json():
        """ export to json """
        dicto = {}
        list_user = []
        user_found = find_user()
        todo_found = find_todo()
        file_json = '{}.json'.format(argv[1])

        u_id = user_found["id"]
        u_username = user_found["username"]

        for d in todo_found[2]:
            dd = {}
            dd['task'] = d["title"]
            dd['completed'] = d["completed"]
            dd['username'] = u_username
            list_user.append(dd)

        dicto[u_id] = list_user

        with open(file_json, 'w') as f:
            json.dump(dicto, f)

    def to_all_json():
        """ export to json """
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        list_all_users = response.json()
        lall = []
        total_list = []
        for a in list_all_users:
            lall.append(a["id"])
        file_json = 'todo_all_employees.json'
        dicto = {}
        for f in lall:
            list_user = []
            user_found = find_user(f)
            todo_found = find_todo(f)

            u_id = user_found["id"]
            u_username = user_found["username"]

            for d in todo_found[2]:
                dd = {}
                dd['task'] = d["title"]
                dd['completed'] = d["completed"]
                dd['username'] = u_username
                list_user.append(dd)

            dicto[u_id] = list_user

        with open(file_json, 'w') as f:
            json.dump(dicto, f)

    to_all_json()
