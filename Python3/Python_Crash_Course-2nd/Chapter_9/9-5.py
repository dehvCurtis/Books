# Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0.

class User:
    def __init__(self, fname, lname, user_name, email, login_attempts):
        self.fname = fname
        self.lname = lname
        self.user_name = user_name
        self.email = email
        self.login_attempts = login_attempts

    def desc_user(self):
        print(f'{self.fname.title()} {self.lname.title()}:')
        print(f'\tUsername: {self.user_name}')
        print(f'\tEmail: {self.email}')
        # print(f'\t{}')

    def greet_user(self):
        print(f'Hello {self.user_name}')

    def increment_login_attempts(self):
        print(f'Current Attempts: {self.login_attempts}')
        self.login_attempts += 2

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'Reset to {self.login_attempts} attempts')

print('Mike:')
user1 = User('Mike','Johnson','test','email@email.com', 5)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

user1.reset_login_attempts()

# Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
print('Molly:')
user2 = User('Molly','Johnson','username','email@email.com', 4)
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()

user2.reset_login_attempts()