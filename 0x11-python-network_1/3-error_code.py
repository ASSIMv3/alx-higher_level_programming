#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""

import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            res_body = response.read()
            print(res_body.decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
