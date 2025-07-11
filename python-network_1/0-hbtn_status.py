#!/usr/bin/python3
import urllib.request
#Module documented
url = "https://intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read().decode("utf-8")
    print("\t- " + body)
