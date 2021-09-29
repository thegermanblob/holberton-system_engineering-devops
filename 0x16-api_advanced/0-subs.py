#!/usr/bin/python3
import json
import requests


def number_of_subscribers(subreddit):
    """ returns number of subs per subreddit """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    head = {'User-Agent': 'requested'}
    response = requests.get(url, headers=head)
    try:
        if response.status_code != 200:
            return 0
        return response.json()['data']['subscribers']
    except:
        return 0