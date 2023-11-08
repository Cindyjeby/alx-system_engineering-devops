#!/usr/bin/python3
"""Redit api"""

import requests


def number of subscribers(subreddit):
"""queary a subredit and retrive number of subs"""
	url = f"https://www.reddit.com/r/{subreddit}/about.json"

	#set a custom user-agent to avoid too many error requests
	headers = {'User-Agent': 'My user Agent 1.0'}

	# send a GET request to the redit api
	response = requests.get(url, headers=headers, allow_redirects=False)

	#check if the response wa successfull and not redirected
	if response.status_code == 200:
		data = response.json().get('data', {})
		sub_count = data.get('subscribers', 0)
		return sub_count
	else:
		return 0
