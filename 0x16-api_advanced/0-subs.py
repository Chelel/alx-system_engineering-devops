#!/usr/bin/python3


import requests

def number_of_subscribers(subreddit):
  """Queries the Reddit API and returns the number of subscribers for a given subreddit.

  Args:
      subreddit: The name of the subreddit to query.

  Returns:
      The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
  """

  # Set a custom User-Agent header to avoid "Too Many Requests" errors
  headers = {'User-Agent': 'my_app/0.1 (by /u/your_username)'}

  # Construct the API URL
  url = f"https://www.reddit.com/r/{subreddit}/about.json"

  # Send a GET request without following redirects
  response = requests.get(url, allow_redirects=False, headers=headers)

  # Check for successful response (status code 200)
  if response.status_code == 200:
    data = response.json()
    # Extract the number of subscribers from the response data
    return data.get('data', {}).get('subscribers', 0)
  else:
    # Invalid subreddit, return 0
    return 0
