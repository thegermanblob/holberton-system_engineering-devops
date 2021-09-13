#!/usr/bin/python3
""" Gets all todo task for an employee and out puts a json file """
from collections import OrderedDict
import json
import requests
import sys


def get_employ(emp_id):
    """ Gets and shows employee completion rate of to-dos """
    url = 'https://jsonplaceholder.typicode.com/'
    emp_r = requests.get(url + 'users/{}'.format(emp_id))
    emp_dict = emp_r.json()
    emp_todo = requests.get(url + 'todos/', params={'userId': emp_id}).json()
    keys = ('title', 'completed', 'username')
    result = []
    json_dict = dict()
    for item in emp_todo:
        result_item = OrderedDict()
        item.pop('id')
        item['username'] = emp_dict.get("username")
        for k in keys:
            if k == "title":
                result_item["task"] = str(item[k])
            else:
                result_item[k] = str(item[k])
        result.append(result_item)

    json_dict[emp_id] = result
    with open("{}.json".format(emp_id), "w") as jsonfile:
        json.dump(json_dict, jsonfile)

if __name__ == "__main__":
    get_employ(sys.argv[1])
