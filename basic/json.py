import json


# with open("json_example.json", "r", encoding="utf8") as f:
#     contents = f.read()
#     json_data = json.loads(contents)
#     print(json_data["employees"])


dic_data = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
with open("data.json", "w") as f:
    json.dump(dic_data, f)
