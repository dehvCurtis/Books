from name_func import get_formatted_name

print('Enter "q" at any time to quit')

while True:
    first = input('Input first name > ')
    if first == 'q':
        break
    last = input('Input last name > ')
    if last == 'q':
        break

    formatted_name = get_formatted_name(first,last)
    print(f'Formatted Name: {formatted_name}')