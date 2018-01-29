#!/usr/bin/env python3
# Jordan huang<good5dog5@gmail.com>

import os
import sys
import subprocess
import csv
import json

db = dict()

with open('db.csv', 'r', encoding='utf-8') as f:
    csvCursor = csv.reader(f)

    for row in csvCursor:
        quest   = row[4]
        ans     = []
        for x in [row[0], row[1], row[2], row[3]]:
            if x:
                ans.append(x) 
        db[quest] = ans

# save the db to json
with open('db.json', 'w') as f:
    json.dump(db, f)
