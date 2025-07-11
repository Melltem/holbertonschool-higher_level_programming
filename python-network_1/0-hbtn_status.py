#!/usr/bin/python3
"""
0-hbtn_status module

Fetches the status from https://intranet.hbtn.io/status using urllib.
Prints the response body type, raw bytes, and UTF-8 decoded content.

Usage:
    Run as a script to display the status response.
"""

import urllib.request

def fetch_status():
    """Fetches and prints the body response from the intranet status URL."""
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    fetch_status()
