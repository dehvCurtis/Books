sandwich_orders = ['tuna','black forest ham','turkey','blt','veggie','meatball']
finished_sandwiches = []


for i in sandwich_orders[:]:
    print(i)
    sandwich_orders.pop()
    finished_sandwiches.append(i)
    print(f'Added {i}')

print(f'Finished: {finished_sandwiches}')