#!/usr/bin/python3
"""
Script that fetches a URL and prints the value of the X-Request-Id header.
"""

import sys
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)
    with request.urlopen(req) as response:
        # Get the 'X-Request-Id' header from the response headers
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
