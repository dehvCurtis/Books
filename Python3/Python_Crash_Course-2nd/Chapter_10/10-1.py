# Write a program that reads the file and prints what you wrote three times. Print the contents once by reading in the entire file
with open('learning_python.txt') as file:
    read_file = file.read()
    print(read_file)

with open('learning_python.txt') as file:
    lines = file.readlines()
    for line in lines:
        print(line * 3)

# once by looping over the file object
with open('learning_python.txt') as file:
    for line in file:
        print(line.rstrip())

# and once by storing the lines in a list and then working with them outside the with block.
l = []
with open('learning_python.txt') as file:
    for line in file:
        l.append(line.strip())
    print(l)
