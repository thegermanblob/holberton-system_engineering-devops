#!/usr/bin/python3
""" module contains top ten func """

import requests


def top_ten(subreddit):
    """ prints the top ten hot posts for a given sub reddit """
    url = 'https://www.reddit.com/r/{}/.json'.format(subreddit)
    head = {"User-Agent": "linux:0x16.api.advanced:v1.0.0"}
    param = {'limit': '10'}
    r = requests.get(url, headers=head, params=param, allow_redirects=False)
    if r.status_code != 200:
        return 0
    r = r.json().get("data")
    for cild in r.get('children'):
        print(cild.get('data').get('title'))
