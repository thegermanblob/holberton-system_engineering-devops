#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """ Gets subscriber count """
    head = {'User-Agent': 'bot9000'}
    r = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers=head, allow_redirects=False)
    if r.status_code != 200:
        return 0
    return r.json()['data']['subscribers']
print (number_of_subscribers('funny'))