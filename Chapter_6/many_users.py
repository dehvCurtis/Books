users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username,user_info in users.items():
    print(f'\nUsername: {username.title()}')
    full_name = f'{user_info["first"]} {user_info["last"]}'

    print(f'\tFull Name: {full_name.title()}')
    print(f'\tLocation: {user_info["location"].title()}')