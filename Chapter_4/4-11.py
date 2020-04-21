# list creation
list = ['pepporoni','sausage','pineapple']

# copying list to new list
friend_list = list[:]

# Add a new pizza to the original list
list.append('cheese')

# Add a different pizza to the list friend_pizzas.
friend_list.append('bacon')

# Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list.

print(f'My fav pizzas:')

for pizza in list:
    print('\t',pizza.title())

# Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list

print(f'My friends fav pizzas:')

for pizza in friend_list:
    print('\t',pizza.title())