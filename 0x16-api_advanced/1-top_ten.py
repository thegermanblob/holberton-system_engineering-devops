#!/usr/bin/python3
""" module contains top ten func """

import requests


def top_ten(subreddit):
    """ prints the top ten hot posts for a given sub reddit """
    url = 'https://www.reddit.com/r/{}/.json'.format(subreddit)
    param = {'limit': '10'}
    r = requests.get(url, params=param, allow_redirects=False)
    if r.status_code != 200:
        return None
    r = r.json().get("data")
    for cild in r.get('children'):
        print(cild.get('data').get('title'))
