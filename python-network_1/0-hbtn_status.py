#!/usr/bin/python3
import urllib.request

url = "https://intranet.hbtn.io/status"
headers = {'User-Agent': 'Mozilla/5.0'}

req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as response:
    body = response.read().decode('utf-8')
    print("Body response:")
    print("\t- {}".format(body))
