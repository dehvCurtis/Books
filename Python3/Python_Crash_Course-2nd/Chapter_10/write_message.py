filename = 'programming.txt'

# with open(filename, 'w') as file:
#     file.write('I love programming\n')
#     file.write('This is a new line')

with open(filename, 'a') as file:
    file.write('I love snowboarding\n')
    file.write('This is a new line')


##
# confirm file write
##
print(f'Printing: {filename}')
with open(filename) as file:
    for line in file:
        print(line.strip())
