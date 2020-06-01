from random import randint

# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and five letters

l = [2,5,6,11,1,6,4,22,33,12,'d','e','s','j','x']

# Randomly select four numbers or letters from the list and print a message saying that any ticket matching these four numbers or letters wins a prize.

count = 0
while count < 4:
    count += 1
    rand_selection = randint(0, 15)
    print(f'Winning Number: {rand_selection}')