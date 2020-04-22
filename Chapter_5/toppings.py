# requested_topping = 'mushrooms'
#
# if requested_topping != 'anchovies':
#     print('Hold the anchovies')

# requested_topping = ['mushrooms','olives']
#
# if 'mushrooms' in requested_topping:
#     print('Adding mushrooms')
# elif 'pepperoni' in requested_topping:
#     print('Adding pep')
# elif 'extra cheese' in requested_topping:
#     print('Extra cheese')
#
# print('Finished making pizza')

# Checking for Special Items
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#
# for topping in requested_toppings:
#     if topping == 'green peppers':
#         print(f'Out of {topping}')
#     else:
#         print(f'Adding {topping}')
#
# print('All done')

# Checking That a List Is Not Empty
requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        print(f'Adding {topping}')
else:
    print('Are you sure you want a plain pizza?')
