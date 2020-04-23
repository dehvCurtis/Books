pizza = {
    'crust':'thick',
    'toppings':['olives','extra cheese'],
}
print(f'You ordered a pizza with {pizza["crust"]} crust. \nYou also requested the following toppings:')
for t in pizza['toppings']:
    print(f'\t- {t}')