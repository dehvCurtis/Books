
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

class Admin(Users):

    def __init__(self,fname,lname,user_name,email):
        super().__init__(fname,lname,user_name,email)
        self.privileges = ['Create','Read','Update','Delete','Sudo']

    def show_privileges(self):
        print(f'User Has The Following Permissions:')
        for permission in self.privileges:
            print(f'\t- {permission}')

# 9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7.

class Privileges:
    def __init__(self):
        self.privileges = ['List','Read']

# Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.

    def show_privileges(self):
        print(f'User Has The Following Permissions:')
        for permission in self.privileges:
            print(f'\t- {permission}')

privilege1 = Admin('Mike','Brown','mbrown','mbrown@mail.com')
privilege2 = Privileges()
privilege2.show_privileges()