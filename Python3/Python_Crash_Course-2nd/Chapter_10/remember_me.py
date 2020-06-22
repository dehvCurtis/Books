import json

filename = 'username1.json'

def get_stored_username():

    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

def greeter():
    username = get_stored_username()

    if username:
        print(f'Welcome back: {username}')
    else:
        username = input('Enter your name > ')
        with open(filename, 'w') as file:
            json.dump(username, file)
            print(f'Added User: {username} to {file}')


greeter()