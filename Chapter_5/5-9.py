# usernames = ['admin','dcurtis','jbrown','llouise','mbrown']
usernames = []

if usernames:
    for name in usernames:
        if name == 'admin':
            print(f'Hello {name}, would you like to see a status report?')
        else:
            print(f'Hello {name}, thank you for logging in')
else:
    print('We need to find some users')