# Make a list of five or more usernames called current_users.
current_users = ['admin','dcurtis','jbrown','llouise','mbrown']

# Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
new_users = ['mdolly','wwaynes','fdavis','Admin','tharding','MBROWN']

# Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.

# for name in new_users:
#     if name in current_users:
#         print(f'The name \'{name}\' is already in use')
#     else:
#         print(f'The username \'{name}\' is available')

# Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

for name in new_users:
    if name.title() in current_users or name.upper() in current_users or name.lower() in current_users:
        print(f'The name \'{name}\' is already in use')
    else:
        print(f'The username \'{name}\' is available')