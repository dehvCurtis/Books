# 9-1
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_name):
#         self.restaurant_name = restaurant_name
#         self.cuisine_name = cuisine_name
#
#     def desc_restaurant(self):
#         print(f'Located in SLC ')
#         print(f'Open Monday through Friday ')
#
#     def open_restaurant(self):
#         print(f'The restaurant is now open')

# restaurant = Restaurant('Mike\'s','Hamburger Meal')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_name)
#
# # 9-2
# restaurant1 = Restaurant('McDonalds','#1')
# print(restaurant1.restaurant_name)
# print(restaurant1.cuisine_name)
# 9-3
# class Users:
#     def __init__(self, fname, lname, user_name, email):
#         self.fname = fname
#         self.lname = lname
#         self.user_name = user_name
#         self.email = email
#
#     def desc_user(self):
#         print(f'{self.fname.title()} {self.lname.title()}:')
#         print(f'\tUsername: {self.user_name}')
#         print(f'\tEmail: {self.email}')
#         # print(f'\t{}')
#
#     def greet_user(self):
#         print(f'Hello {self.user_name}')

# 9-4 INCOMPLETE
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

restraunt = Restaurant('Mike\'s Burgers','Buger Meal')
restraunt.increment_num_served()