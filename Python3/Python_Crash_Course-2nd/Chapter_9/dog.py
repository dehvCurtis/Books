
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


my_dog = Dog('Tido',3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

your_dog = Dog('Kitty',5)
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")