#!/usr/bin/python3
# -*- coding: latin-1 -*-

import json
import sys

with open(sys.argv[1], encoding='latin-1') as f:
    data = json.load(f)
    print(json.dumps(data, indent=2))
