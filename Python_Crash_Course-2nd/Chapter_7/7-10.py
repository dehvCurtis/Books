# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where would you go?
# Include a block of code that prints the results of the poll.

countries = []

prompt = 'If you could visit anywhere in the world, where would you visit?\n'
prompt += '> '
active = True

while active:
    answer = input(prompt)
    if answer != 'quit':
        print(f'Adding {answer} to list')
        countries.append(answer)
        print(countries)
    elif answer == 'quit':
        print(f'List complete')
        for i in countries:
            print(f'\t{i}')
        active = False