#!/usr/bin/python3
"""Module documented"""
import urllib.request
url = "https://intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read().decode("utf-8")
    print("\t- " + body)
