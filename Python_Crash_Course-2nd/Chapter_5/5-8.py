usernames = ['admin','dcurtis','jbrown','llouise','mbrown']

# If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again

for name in usernames:
    if name == 'admin':
        print(f'Hello {name}, would you like to see a status report?')
    else:
        print(f'Hello {name}, thank you for logging in')