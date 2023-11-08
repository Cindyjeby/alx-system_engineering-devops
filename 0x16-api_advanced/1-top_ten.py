#!/usr/bin/python3
"""sub reddit"""

import requests

def top_ten(subreddit):
	"""query reddit and print titles of the first 10 hot posts"""

	url = f"https://www.reddit.com/r/{subreddit}/hot.json"

	#set custiom user-agent to avoid too many requests error
	headers = {'User-Agent': 'My user Agent 1.0'}

	#send GET request
	response = requests.get(url, headers=headers, allow_redirects=False)

	try:
		response = requests.get(url, headers=headers,
					allow_redirects=False)
		if response.status_code == 200:
			children = response.json().get('data').get('children')
			for k = range(10):
				print(children[k].get('data').get('title'))
		else:
			print("None")
	except Exception:
		print("None")
