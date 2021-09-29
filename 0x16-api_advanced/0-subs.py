#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """ Gets subscriber count """
    head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61\
               Safari/537.36'}
    r = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers=head, allow_redirects=False)
    if r.status_code is not 200:
        return 0
    return r.json()['data']['subscribers']
