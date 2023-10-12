#!/usr/bin/python3
"""Recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns top ten post titles recursively"""
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 25, 'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)
    if results.status_code == 200:
        data = results.json()

        for item in data['data']['children']:
            hot_list.append(item['data']['title'])

            last_submission = data['data']['after']

            if last_submission:
                return recurse(subreddit, hot_list, after=last_submission)
            else:
                return hot_list
    else:
        return None
