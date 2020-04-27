# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['tuna','black forest ham','pastrami','blt','pastrami','meatball','pastrami']
finished_sandwiches = []

print('Deli is out of pastrami')

for i in sandwich_orders[:]:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
        print(sandwich_orders)

for i in sandwich_orders[:]:
    print(i)
    sandwich_orders.pop()
    finished_sandwiches.append(i)
    print(f'Added {i}')

print(f'Finished: {finished_sandwiches}')