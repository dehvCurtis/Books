guest_list = ['Michael Jordan','Madonna','Stephen King']

for name in guest_list:
    print('Invite to Dinner for: ', name)

print(f'It seems that {guest_list[1]} cannot attend')

guest_list[1] = 'Britney Spears'

for name in guest_list:
    print('Invite to Dinner for: ', name)

print('3 more spaces available')

guest_list.append('Governor')
guest_list.append('Mayor')
guest_list.append('President')

print(f'New Guest List: {guest_list}')

for name in guest_list:
    print('Invite to Dinner for: ', name)

print('Looks like we can only have two guests')

guest_list.pop(-1)
print(guest_list)
guest_list.pop(-1)
print(guest_list)
guest_list.pop(-1)
print(guest_list)
guest_list.pop(-1)
print(guest_list)

del guest_list[1]
del guest_list[0]
print(guest_list)