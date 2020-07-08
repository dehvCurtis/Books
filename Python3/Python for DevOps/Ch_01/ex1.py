def first_name():
    first = input('What is your first name > ')
    if first == '':
        exit()
    else:
        print(f'Hello {first.title()}, nice to meet you')

first_name()