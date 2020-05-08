states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}
cities = {
    'FL': 'Miami',
    'CA':'San Fran',
    'MI':'Detroit',
}

cities['NY'] = 'New York City'
cities['OR'] = 'Salem'

print('-' * 10)

print(f'NY State has: {cities["NY"]}')
print(f'OR state has: {cities["OR"]}')

print('-' * 10)

print(f'Michigan abbrev is: {states["Michigan"]}')
print(f'California abbrev is: {states["California"]}')

print('-' * 10)

print(f'Michigan has: {cities[states["Michigan"]]}')
print(f'New York has: {cities[states["New York"]]}')

print('-' * 10)

for state, abbrev in list(states.items()):
    print(state + "-" + abbrev)

print('-' * 10)

for abbrev, city in list(cities.items()):
    print(f'{abbrev} has the city {city}')

print('-' * 10)

for state, abbrev in list(states.items()):
    print(f'{state} is abbreviated like this: {abbrev}')
    print(f'{state} has the city {cities[abbrev]}')

print('-' * 10)

state1 = states.get('Texas')
state2 = states.get('Oregon')

if not state1:
    print(f'Sorry no Texas')
elif not state2:
    print(f'Sorry no Oregon')

print('-' * 10)

city = cities.get('TX','Does not exist')
print(f'The city for "TX" is {city}')