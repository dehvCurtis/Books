# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
age = input('Enter your age > ')
age = int(age)
if age == 0:
    print(f'Sorry that\'s not an age.')
    exit(0)

# If a person is under the age of 3, the ticket is free;
if age < 3:
    print(f'You get a free ticket')

# if they are between 3 and 12, the ticket is $10;
elif age >= 3 and age <= 12:
    print(f'Your ticket will be $10')

# if they are over age 12, the ticket is $15.
elif age > 12:
    print('Your ticket will be $15')

