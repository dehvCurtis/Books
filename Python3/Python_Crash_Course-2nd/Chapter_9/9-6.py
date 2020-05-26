class Restaurant:
    def __init__(self,restaurant_name,cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name
        self.number_served = 0

    def desc_restaurant(self):
        print(f'Located in SLC ')
        print(f'Open Monday through Friday ')

    def open_restaurant(self):
        print(f'The restaurant is now open')

    def num_served(self):
        print(f'Number Served: {self.number_served}')

    def set_num_served(self):
        served = input('Please set a number > ')
        print(f'Number Served: {served}')

    def increment_num_served(self):
        print(f'Number Served: {self.number_served}')
        inc_number = input('Enter number to increment > ')
        self.number_served = self.number_served + int(inc_number)
        print(f'New number served: {self.number_served}')

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167).
# Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_name='ice cream'):
        super().__init__(restaurant_name,cuisine_name)
        self.flavors = []

    def display_flavors(self):
        print(f'Flavors:')
        for flav in self.flavors:
            print(f'- {flav}')

mikes = IceCreamStand('mikes')
mikes.flavors = ['vanilla','chocoloate','strawberry']
mikes.display_flavors()