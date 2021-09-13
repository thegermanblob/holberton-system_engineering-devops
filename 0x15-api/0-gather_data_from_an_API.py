#!/usr/bin/python3
""" gets emplyee complition of todos """
import requests
import sys


def get_employ(emp_id):
    """ Gets and shows employee completion rate of to-dos """
    url = 'https://jsonplaceholder.typicode.com/'
    emp_r = requests.get(url + 'users/{}'.format(emp_id))
    emp_dict = emp_r.json()
    emp_todo = requests.get(url + 'todos/', params={'userId': emp_id}).json()
    todo_comp = 0
    comp_task = []
    for item in emp_todo:
        if item.get('completed'):
            todo_comp += 1
            comp_task.append(item.get('title'))
    print ('Employee {} is done with tasks({}/{}):'
           .format(emp_dict.get("name"), todo_comp, len(emp_todo)))
    for item in comp_task:
        print("\t {}".format(item))


if __name__ == "__main__":
    get_employ(sys.argv[1])

