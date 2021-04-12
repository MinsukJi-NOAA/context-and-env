#!/usr/bin/env python3

import os
import re
import sys
import json
import time
from urllib.request import urlopen, Request

def main():

  url = sys.stdin.read()
  token = os.environ.get('AUTH')

  print(token)

  request = Request(url)
  request.add_header('Authorization', 'token %s' % token)
  response = urlopen(request)

  print(response.info())

  data = json.loads(response.read().decode())
  print(json.dumps(data, indent=4))

if __name__ == "__main__": main()
