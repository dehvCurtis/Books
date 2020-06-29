
import json

filename = 'numbers.json'

try:
    with open('favorite_number.json') as file:
        number = json.load(file)
except FileNotFoundError:
    number = input("What's your favorite number? ")
    with open('favorite_number.json', 'w') as file:
        json.dump(number, file)
    print("Thanks, I'll remember that.")
else:
    print("I know your favorite number! It's " + str(number) + ".")
