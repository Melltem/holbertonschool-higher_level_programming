#!/usr/bin/python3
"""
Module documented
"""

import urllib.request

url = "https://intranet.hbtn.io/status"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as response:
    body = response.read().decode("utf-8")
    print("\t- " + body)
