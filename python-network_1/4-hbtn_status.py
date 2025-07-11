#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status and displays the body with formatting.
"""

import requests

if __name__ == "__main__":
    """Ensure code is executed when directly run"""
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.text
    print("Body response:")
    print(f"\t- {body}")
