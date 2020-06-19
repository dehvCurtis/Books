

print('Enter two numbers to divide')
print('Enter \'quit\' to exit')

while True:
    first_number = input('Enter first number: ')
    if first_number == 'q':
        break
    second_number = input('Enter second number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
        print(answer)
    except ZeroDivisionError:
        print('Cannot divide by zero!')
