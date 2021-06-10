# def wh_loop(starting_num, increment_num):
#     i = 0
#     numbers = []

#     while i < starting_num:
#         print(f'At the top i is {i}')
#         numbers.append(i)

#         i = i + increment_num
#         print(f'Numbers now: ', numbers)
#         print(f'After the bottom i is {i}')

#     print(f'The numbers: ')

#     for num in numbers:
#         print(num)

# wh_loop(6, 2)

# rewrite with for loop

def for_loop(starting_num, increment_num):
    i = 0
    numbers = []

    for num in range(0,10):
        print(f'At the top i is {i}')
        numbers.append(i)

        i = i + increment_num
        print(f'Numbers now: {i}')
        print(f'After bottom is: {i}')
    
    print(f'The numbers: ')

    for num in numbers:
        print(num)

for_loop(2,9)