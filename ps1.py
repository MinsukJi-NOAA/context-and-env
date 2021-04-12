#!/usr/bin/env python3

import re
import sys
import json
import time
from urllib.request import urlopen

def main():

  url = sys.stdin.read()
  response = urlopen(url)
  data = json.loads(response.read().decode())
  print(json.dumps(data, indent=4))

if __name__ == "__main__": main()
