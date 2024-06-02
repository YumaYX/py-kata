import json

data = {"a":1,"b":True,"c":[]}

with open("sample.json", "w") as json_file:
    json.dump(data, json_file)

with open("sample.json", "r") as json_file:
    data = json.load(json_file)
    print(type(data))

    for key, value in data.items():
        print(key + ":", value)
