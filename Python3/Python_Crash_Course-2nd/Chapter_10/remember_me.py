import json

filename = 'username1.json'

try:
    with open(filename) as file:
        f = json.load(file)
        print(f'Welcome back {f}')

except FileNotFoundError:
    print('file not found')
    username = input('What is your name > ')
    with open(filename, 'w') as file:
        json.dump(username, file)
        print(f'Registered user: {username}')