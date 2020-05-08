guest_list = ['Michael Jordan','Madonna','Stephen King']

for name in guest_list:
    print('Invite to Dinner for: ', name)

print(f'It seems that {guest_list[1]} cannot attend')

guest_list[1] = 'Britney Spears'

for name in guest_list:
    print('Invite to Dinner for: ', name)