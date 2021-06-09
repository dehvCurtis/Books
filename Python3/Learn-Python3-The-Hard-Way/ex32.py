the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

# lists all numbers in list
for number in the_count:
    print(f'This is the number: {number}')

# lists all fruit in list
for fruit in fruits:
    print(f'This is the fruit: {fruit}')

# lists all items in mixed list
for item in change:
    print(f'This is the item: {item}')

# build list example
elements = []

for i in range(0,6):
    print(f'Adding {i} to the elements list')
    elements.append(i)

# print list
print(f'printing the elements list: {elements}')