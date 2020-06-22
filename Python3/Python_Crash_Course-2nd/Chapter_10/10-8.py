# Make two files, cats.txt and dogs.txt.
#
# Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block executes properly.

# filename = 'cats.txt'
filename = 'dogs.txt'
# filename = 'humans.txt'

def read_file():
    try:
        with open(filename) as cat_file:
            for line in cat_file:
                print(line.rstrip().title())
    except FileNotFoundError:
        print(f'The filename "{filename}" not found!')


read_file()