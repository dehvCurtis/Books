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