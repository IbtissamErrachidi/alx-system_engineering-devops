#!/usr/bin/python3
"""
Recursively retrieves a list of titles of all hot posts
on a given subreddit.
"""


import requests

def recurse(subreddit, hot_list=[], after=None):
    base_url = 'https://www.reddit.com/r/{}/hot.json'
    params = '?limit=100&after={}'
    url = (base_url + params).format(subreddit, after)
    headers = {'User-Agent': 'Custom User Agent'}  # Custom User-Agent to avoid errors

    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return None
    data = response.json()
    posts = data['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])
        
    after = data['data']['after']
    if after:
        recurse(subreddit, hot_list, after)
    else:
       return hot_list
