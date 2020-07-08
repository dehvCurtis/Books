# Write a Python function that takes a name as an argument and prints that name.

def first_name():
    first = input('What is your first name > ')
    if first == '':
        exit()
    else:
        print(f'Hello {first.title()}, nice to meet you')

first_name()