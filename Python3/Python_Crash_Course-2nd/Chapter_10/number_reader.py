import json

with open('numbers.json') as file:
    num = json.load(file)

print(num)