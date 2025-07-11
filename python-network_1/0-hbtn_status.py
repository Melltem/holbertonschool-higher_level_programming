#!/usr/bin/env python3
import urllib.request

url = "https://intranet.hbtn.io/status"

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection': 'keep-alive'
}

req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as response:
    body = response.read().decode('utf-8')
    print("Body response:")
    print("\t- {}".format(body))
