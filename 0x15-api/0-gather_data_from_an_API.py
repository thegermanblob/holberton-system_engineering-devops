#!/usr/bin/python3
import requests
import sys


def get_employ(emp_id):
    """ Gets and shows employee completion rate of to-dos """
    url = 'https://jsonplaceholder.typicode.com/'
    emp_r = requests.get(url + 'users/{}'.format(emp_id))
    emp_dict = emp_r.json()
    emp_todo = requests.get(url + 'todos/', params={'userId': emp_id}).json()
    todo_comp = 0
    for item in emp_todo:
        if item['completed']:
            todo_comp += 1
    print ('Employee {} is done with tasks({}/{}):'
           .format(emp_dict["name"], todo_comp, len(emp_todo)))


if __name__ == "__main__":
    get_employ(sys.argv[1])
