#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status and displays the body with formatting"""
import requests

if __name__ == "__main__":
    """Ensure code is executed when directly run"""
    url = "https://intranet.hbtn.io/status"
    headers = {'cfclearance': 'true'}
    response = requests.get(url, headers=headers)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
