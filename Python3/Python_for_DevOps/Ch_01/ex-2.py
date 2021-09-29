# Write a Python function that takes a string as an argument and prints whether it is upper- or lowercase.

def upper_lower(string):
    if string == string.upper():
        print('UPPERCASE')
    elif string == string.lower():
        print('lowercase')

upper_lower('THIS')
upper_lower('this')