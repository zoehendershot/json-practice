#!/usr/bin/env python3
import json

with open('data/schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'w') as csv_file:
    for repo in data[:5]:
        csv_file.write(f"{repo['name']},{repo['html_url']},{repo['updated_at']},{repo['visibility']}\n")
