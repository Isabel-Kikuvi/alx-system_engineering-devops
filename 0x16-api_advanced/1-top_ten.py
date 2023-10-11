#!/usr/bin/python3
"""prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "Custom User Agent"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'children' in data['data']:
                posts = data['data']['children']
                for post in posts:
                    title = post['data']['title']
                    print(title)
        else:
            print(None)
    except Exception as e:
        print(None)
