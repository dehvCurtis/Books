from sys import argv

script, filename = argv

print(f'We\'re going to erase {filename}')
print('If you don\'t want that, hit CTRL-C (^C)')
print(f'To erase {filename}, hit RETURN')

input('...')

print('Opening the file...')
target = open(filename, 'w')

print('Truncating file...')
target.truncate()

print('Now I\'m going to ask you for three lines:')

line1 = input('line 1: ')
line2 = input('line 2: ')
line3 = input('line 3: ')

print('Writing to file...')

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print('Closing file...')
target.close()