# requested_topping = 'mushrooms'
#
# if requested_topping != 'anchovies':
#     print('Hold the anchovies')

requested_topping = ['mushrooms','olives']

if 'mushrooms' in requested_topping:
    print('Adding mushrooms')
elif 'pepperoni' in requested_topping:
    print('Adding pep')
elif 'extra cheese' in requested_topping:
    print('Extra cheese')

print('Finished making pizza')