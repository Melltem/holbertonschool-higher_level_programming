#!/usr/bin/python3
"""
Uses GitHub API and Basic Auth to display user id.
"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, token))
    try:
        user_data = response.json()
        print(user_data.get("id"))
    except ValueError:
        print("Not a valid JSON")
