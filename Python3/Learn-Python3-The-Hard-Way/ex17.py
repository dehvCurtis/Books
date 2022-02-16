from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f'Copying file: {from_file} to file: {to_file}')

in_file = open(from_file)
indata = in_file.read()

print(f'The input file is {len(indata)} bytes long')

print(f'Does the output file exist? {exists(to_file)}')
print('Ready, hit RETURN to continue')
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print('Complete')

out_file.close()
in_file.close()