import json

# Opening JSON file
f = open(file="test\\test1.json", mode='r')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['ip']:
    print(i)

# Closing file
f.close()