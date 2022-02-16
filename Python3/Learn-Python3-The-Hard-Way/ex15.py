# imports libs
from sys import argv

#creates agrument variables (script being used and user defined filename)
script, filename = argv

#opens file and saves it to variable
txt = open(filename)

#pritns filename
print(f"Here's your file: {filename}")
print(txt.read())

#prints filename again (or new)
print('Type the filename again:')
file_again = input('> ')

#opens filename
txt_again = open(file_again)

#reads filename
print(txt_again.read())

# close files
txt.close()
txt_again.close