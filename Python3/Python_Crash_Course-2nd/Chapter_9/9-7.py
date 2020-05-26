

class Users:
    def __init__(self, fname, lname, user_name, email):
        self.fname = fname
        self.lname = lname
        self.user_name = user_name
        self.email = email

    def desc_user(self):
        print(f'{self.fname.title()} {self.lname.title()}:')
        print(f'\tUsername: {self.user_name}')
        print(f'\tEmail: {self.email}')
        # print(f'\t{}')

    def greet_user(self):
        print(f'Hello {self.user_name}')

# 9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167)

class Admin(Users):

# Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.

    def __init__(self,fname,lname,user_name,email):
        super().__init__(fname,lname,user_name,email)
        self.privileges = ['Create','Read','Update','Delete','Sudo']

    def show_privileges(self):
        print(f'User Has The Following Permissions:')
        for permission in self.privileges:
            print(f'\t- {permission}')

mike = Admin('Mike','Brown','mbrown','mbrown@mail.com')
mike.show_privileges()

