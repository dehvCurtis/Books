
while True:
    try:
        num_one = input('Type a number > ')
        if num_one == 'q':
            break
        num_one = int(num_one)
        num_two = input('Type a number > ')
        if num_two == 'q':
            break
        num_two = int(num_two)
    except ValueError:
        print(f'Not a number')

    else:
        print(num_one + num_two)