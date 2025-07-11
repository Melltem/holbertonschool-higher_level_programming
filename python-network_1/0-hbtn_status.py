#!/usr/bin/python3
"""Module documented"""

import urllib.request

url = "https://intranet.hbtn.io/status"

req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(req) as response:
    body = response.read().decode("utf-8")
    print("\t- " + body)
