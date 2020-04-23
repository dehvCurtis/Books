people = {
    'jbrown':{
        "fname":"jake",
        "lname":"brown",
        "age":"34",
        "city":"salt lake city"
    },
    'aeinstein': {
        'fname': 'albert',
        'lname': 'einstein',
        'age': '44',
        'city': 'rio de janiero'
    },

    'mcurie': {
        'fname': 'marie',
        'lname': 'curie',
        'age': '28',
        'city': 'london'
    }
}

for person,user in people.items():
    full_name = f'{user["fname"].title()} {user["lname"].title()}'
    age = f'{user["age"]}'
    city = f'{user["city"]}'
    print(f'\nFull Name: {full_name}')
    print(f'Age: {age}')
    print(f'City: {city.title()}')
