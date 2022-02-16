import json
import os
import sys

if __name__ == "__main__":
    latest_release = json.load(sys.stdin)[0]["assets"]
    for asset in latest_release:
        if "linux" in asset["name"]:
            print(asset["browser_download_url"])
            break
