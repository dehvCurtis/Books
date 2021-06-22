ten_things = "Apples Oranges Crows Telephone Computer"

print('Wait there are not 10 things, let\'s fix that')

stuff = ten_things.split()
more_stuff = ['Day','Night','Shovel','Dog','Cat','Book','TV']

while len(ten_things) != 10:
    next_one = more_stuff.pop()
    print(f'Adding: {next_one}')
    stuff.append(next_one)
    print(f'There are {len(stuff)} now')

print("There we go: ", stuff)