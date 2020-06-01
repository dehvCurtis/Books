from user import Users

class Admin(Users):

    def __init__(self,fname,lname,user_name,email):
        super().__init__(fname,lname,user_name,email)
        self.privileges = ['Create','Read','Update','Delete','Sudo']

    def show_privileges(self):
        print(f'User Has The Following Permissions:')
        for permission in self.privileges:
            print(f'\t- {permission}')