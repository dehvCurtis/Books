
class Dog:
    """ model a dog """

    def __init__(self, name, age):
        # initialize name and age attributes
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is now sitting')

    def rollover(self):
        print(f'{self.name} is rolling over')