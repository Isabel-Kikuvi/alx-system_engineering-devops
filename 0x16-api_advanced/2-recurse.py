#!/usr/bin/python3
"""ecursive function that queries the Reddit API"""
import requests
after = None


def recurse(subreddit, hot_list=None):
    """returns a list containing the titles of all hot articles
    for a given subreddit"""
    global after
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'after': after}
    headers = {
        "User-Agent": "Custom User Agent"
    }
    response = requests.get(url, params=parameters, headers=headers,
                            allow_redirects=False)
    if response.status_code == 200:
        after_data = response.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = response.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
