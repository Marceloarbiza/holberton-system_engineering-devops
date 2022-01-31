#!/usr/bin/python3
""" JSon API """


if __name__ == "__main__":
    import csv
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
        todos_true = []
        todos_totales = []
        count_totales = 0
        response = requests.get('https://jsonplaceholder.typicode.com/todos')
        list_todo = response.json()

        for todo in list_todo:
            if todo['userId'] == int(argv[1]):
                todos_totales.append(todo)
                count_totales += 1
            if todo['userId'] == int(argv[1]) and todo['completed'] is True:
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

    to_csv()
