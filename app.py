import json 


import json

with open('Raw Consumption Data.json', encoding="utf-8") as f:
  data = json.load(f)


with open('output.jsonl', 'w') as outfile:
    for i in data:
        json.dump(i, outfile)
        outfile.write('\n')
    
