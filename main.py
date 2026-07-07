import requests
import csv
import json

from datetime import datetime

with open("config.json") as configfile:
    config = json.load(configfile)

website_ids = config["website_ids"]
umamiBase = config["umamiBaseUrl"]

with open(config["logfile"]) as f:
    reader = csv.DictReader(f,["website", "userAgent", "timestamp", "ip"], delimiter='\t')
    for line in reader:
        line["hostname"] = line["website"][8:-1]
        line["website"] = website_ids[line["website"]]
        line["timestamp"] = int(datetime.fromisoformat(line["timestamp"]).timestamp())
        line["ip"] = line["ip"].split(":")[0]
        useragent = line["userAgent"]
        line.pop("userAgent")
         
        print(f"Uploading: {line}")

        result = requests.post(umamiBase + "/api/send/", 
                      headers={'Content-Type': 'application/json',
                                'User-Agent':useragent},
                      json={"type": "event", "payload": line})
        print(f"Result: {result.status_code}")