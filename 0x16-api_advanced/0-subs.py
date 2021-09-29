#!/usr/bin/python3
import requests

def number_of_subscribers(sub):
    """ Gets subscriber count """
    head = {'User-Agent': 'requested'}
    r = requests.get('https://www.reddit.com/r/{}/about.json'.format(sub), headers=head)
    if r.status_code > 299:
        return 0
    return r.json()['data']['subscribers']
