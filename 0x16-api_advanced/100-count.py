#!/usr/bin/python3
"""
a recursive function that queries the Reddit API to get the titles of all popular (hot) articles
"""
import requests

def count_words(subreddit, word_list, after=None, counts={}):
    base_url = 'https://www.reddit.com/r/{}/hot.json'
    params = '?limit=100&after={}'
    url = (base_url + params).format(subreddit, after)
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1

        after = data['data']['after']
        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print("Invalid subreddit or no posts found.")
