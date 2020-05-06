# Defining a Function
# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")
#
# greet_user()

# Passing Information to a Function
# def greet_user(username):
#     """ DISPLAYS GREETING """
#     print(f'Hello {username.title()}')
# greet_user('bill')

# Using a Function with a while Loop
def get_formatted_name(first_name,last_name):
    """ Return a full name, neatly formatted. """
    full_name = f'{first_name} {last_name}'
    return full_name.title()

while True:
    print('\nPlease type your name or \'quit\'')
    fname = input('First Name > ')
    if fname == 'quit':
        break
    lname = input('Last Name > ')
    if lname == 'quit':
        break

    formatted_name = get_formatted_name(fname,lname)
    print(f'Hello {formatted_name}')
