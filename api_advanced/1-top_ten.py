#!/usr/bin/python3
"""Queries the Reddit API and prints the top 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/120.0 Safari/537.36"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        posts = response.json().get("data").get("children")
        titles = [p.get("data").get("title") for p in posts]
    except (AttributeError, TypeError, ValueError):
        print(None)
        return
    for title in titles:
        print(title)
