
import json

filename = 'numbers.json'
numbers = []
num = input('Input number or type "done": ')

with open(filename, 'w') as file:
    if num == "done":
        exit(0)
    elif num != "done":
        numbers.append(num)
    json.dump(numbers, file)

with open(filename) as file:
    for line in file:
        print(line)