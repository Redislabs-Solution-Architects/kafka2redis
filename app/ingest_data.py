# Python program to read
# json file
 
from utility import redis_conn
import json
 
# Opening JSON file
f = open('app/resources/test_data.json')
 
# returns JSON object as 
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
for item in data:
    print(item)
    key = f'transaction:{item["id"]}'
    date = item["date"]
    redis_conn.json().set(key, "$", item)
 
# Closing file
f.close()