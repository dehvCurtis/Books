import json

numbers = [1,3,5,6,7,8,9]
filename = 'numbers.json'

with open(filename, 'w') as file:
    json.dump(numbers,file)