#!/usr/bin/python3
"""queries subscribers for a reddit"""

import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers for a given
    subreddit. If an invalid subreddit is given, the function should return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Custom User Agent"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except Exception as e:
        return 0
