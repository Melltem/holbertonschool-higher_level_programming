#!/usr/bin/python3
"""
Fetches a URL and displays the response body.
Handles HTTPError exceptions.
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
