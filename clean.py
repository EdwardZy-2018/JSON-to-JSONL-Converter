import json


import json

with open('Raw Consumption Data.json', encoding="utf-8") as f:
  data = json.load(f)
  for i in data:
      i['receipt_desc'].replace("\n", " ")
