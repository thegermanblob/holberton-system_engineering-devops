#!/usr/bin/python3
""" Gets all todo task for an employee and out puts a json file """
from collections import OrderedDict
import json
import requests
import sys


def get_employ():
    """ Gets and shows employee completion rate of to-dos """
    url = 'https://jsonplaceholder.typicode.com/'
    emp_r = requests.get(url + 'users/')
    emp_dict = emp_r.json()
    json_dict = dict()
    for i in range(len(emp_dict)):
        emp_todo = requests.get(url + 'todos/',
                                params={'userId': emp_dict[i]['id']}).json()
        keys = ('username', 'title', 'completed')
        result = []
        for item in emp_todo:
            result_item = OrderedDict()
            item.pop('id')
            item['username'] = emp_dict[i].get("username")
            for k in keys:
                if k == "title":
                    result_item["task"] = str(item[k])
                else:
                    result_item[k] = str(item[k])
            result.append(result_item)

        json_dict[emp_dict[i].get('id')] = result
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(json_dict, jsonfile)
if __name__ == "__main__":
    get_employ()
