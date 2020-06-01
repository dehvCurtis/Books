import random

class Dice:

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        print(f'Dice Roll: ', random.randint(0,self.sides))


    def roll_die_10(self,roll_die,turns=0):

        for i in range(0,turns):
            print(f'Dice Roll: ', random.randint(0,self.sides))




# d6 = Dice()
# d6.roll_die_10(6)

d10 = Dice()
d10.roll_die_10(6,4)