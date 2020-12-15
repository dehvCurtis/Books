# Python for DevOps
# Chapter 1

# Write a Python function that takes a string as an argument and prints whether it is upper- or lowercase.

def upper_lower(string):
    print(f'The string is {string}')
    if string == string.upper():
        print('It\'s upper')
    elif string == string.lower():
        print('It\'s lower')
    else:
        print('Unknown')

upper_lower('HELLO')