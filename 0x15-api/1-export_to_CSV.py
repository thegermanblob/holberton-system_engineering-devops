#!/usr/bin/python3
""" exports the tasks for an employee to csv """
import csv
from collections import OrderedDict
import requests
import sys


def get_employ(emp_id):
    """ Gets and shows employee completion rate of to-dos """
    url = 'https://jsonplaceholder.typicode.com/'
    emp_r = requests.get(url + 'users/{}'.format(emp_id))
    emp_dict = emp_r.json()
    emp_todo = requests.get(url + 'todos/', params={'userId': emp_id}).json()
    keys = ('userId', 'username', 'completed', 'title')
    result = []
    for item in emp_todo:
        result_item = dict()
        item.pop('id')
        item['username'] = emp_dict["username"]
        for k in keys:
            result_item[k] = str(item[k])
        result.append(result_item)
    with open('USER_ID.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile,
                                fieldnames=keys, quoting=csv.QUOTE_ALL)
        writer.writerows(result)

if __name__ == "__main__":
    get_employ(sys.argv[1])
