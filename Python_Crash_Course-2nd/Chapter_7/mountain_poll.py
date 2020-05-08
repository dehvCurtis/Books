responses = {}

polling = True

while polling:
    name = input('Please input name: ')
    color = input('Please input color: ')

    responses[name] = color

    repeat = input('Keep going? ')
    if repeat == 'no':
        polling = False

print(f'Polling complete')
print(responses)