import json

filename = 'username.json'

with open(filename) as file:
    user = json.load(file)
    print(f'Welcome back {user}')