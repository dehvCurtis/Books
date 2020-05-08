# list creation
the_count = [1,2,3,4]
fruits = ['apples','oranges','pears','apricots']
change = [1, "pennies", 2, "dimes", 3, "quarters"]

# loop to count numbers in the_count
for n in the_count:
    print(f"Number {n}")

# loop to list fruit
for f in fruits:
    print(f"Fruit Name: {f}")

# loop to list change
for c in change:
    print(f"Change: {c}")

# init empty list
elements = []

# add number 0-6 to list
for i in range(0,6):
    print(f"Adding {i} to list")
    elements.append(i)

# print list
for i in elements:
    print(f"Here's your list: {i}")
