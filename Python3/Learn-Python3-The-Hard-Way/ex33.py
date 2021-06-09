i = 0
numbers = []

while i < 6:
    print(f'At the top i is {i}')
    numbers.append(i)

    i = i + 1
    print(f'Numbers now: ', numbers)
    print(f'After the bottom i is {i}')

print(f'The numbers: ')

for num in numbers:
    print(num)