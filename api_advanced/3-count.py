#!/usr/bin/python3
"""Recursively counts keywords in the hot post titles of a subreddit."""
import requests


def count_words(subreddit, word_list, instances=None, after=None):
    """Prints a sorted count of the given keywords found in hot titles."""
    if instances is None:
        instances = {}
    words = [w.lower() for w in word_list]
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0 (by /u/student)"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get("data", {})
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for token in title.lower().split():
            if token in words:
                instances[token] = instances.get(token, 0) + 1
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, instances, after)
    results = sorted(((w, c * words.count(w)) for w, c in instances.items()),
                     key=lambda item: (-item[1], item[0]))
    for word, count in results:
        print("{}: {}".format(word, count))
