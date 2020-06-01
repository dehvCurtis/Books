from random import randint
l = [2,5,6,11,1,6,4,22,33,12]
# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket

my_ticket = [2,11,1,6]

# Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.

winning_numbers = []
while winning_numbers != my_ticket:
    i = 0
    rand_selection = randint(0,15)
    winning_numbers.append(rand_selection)