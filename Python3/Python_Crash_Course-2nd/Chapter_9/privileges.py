class Privileges:
    def __init__(self):
        self.privileges = ['List','Read']

    def show_privileges(self):
        print(f'User Has The Following Permissions:')
        for permission in self.privileges:
            print(f'\t- {permission}')