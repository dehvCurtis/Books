pizza_toppings = []
active = True

while active == True:
    topping_input = input('Please pick a topping > ')

    if topping_input != 'quit':
        pizza_toppings.append(topping_input)
        print(f'You selected the following toppings:')
        for topping in pizza_toppings:
            print(f'\t - ', topping)
    elif topping_input == 'quit':
        active = False
        print(f'You selected the following toppings:')
        for topping in pizza_toppings:
            print(f'\t - ', topping)