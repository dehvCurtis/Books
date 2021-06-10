def wh_loop(starting_num, increment_num):
    i = 0
    numbers = []

    while i < starting_num:
        print(f'At the top i is {i}')
        numbers.append(i)

        i = i + increment_num
        print(f'Numbers now: ', numbers)
        print(f'After the bottom i is {i}')

    print(f'The numbers: ')

    for num in numbers:
        print(num)

wh_loop(6, 2)