# Write a program that prompts for two numbers. Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.

try:
    num_one = input('Type a number > ')
    num_one = int(num_one)
    num_two = input('Type a number > ')
    num_two = int(num_two)
except ValueError:
    print(f'Not a number')

else:
    print(num_one + num_two)