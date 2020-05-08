# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# lang = favorite_languages['sarah'].title()
# print(f'Sarah\'s fav language is: {favorite_languages["sarah"].title()}')

# Looping Through All Key-Value Pairs
# for k,v in favorite_languages.items():
#     print(f'{k.title()}\'s favorite language is {v.title()}')

# Looping Through All the Keys in a Dictionary
# for k in favorite_languages:
#     print(f'{k}')

# friends = ['phil','sarah']
# for name in favorite_languages:
#     print(f'Hi there {name.title()}')
#     if name == 'phil' or name == 'sarah':
#         print(f'\t{name.title()}, I see you enjoy {favorite_languages[name].title()}')

# Looping Through a Dictionary’s Keys in a Particular Order
# for name in sorted(favorite_languages.keys()):
#     print(f'{name.title()}, thanks for taking the poll')

# Looping Through All Values in a Dictionary
# for value in favorite_languages.values():
#     print(value.title())

# Remove duplicates
# for value in set(favorite_languages.values()):
#     print(value.title())

favorite_languages = {
    'jen': ['python','c++'],
    'sarah': ['c','.net','rust'],
    'edward': 'ruby',
    'phil': 'python'
}

for name,lang in favorite_languages.items():
    print(f'{name.title()} loves')
    for lang1 in lang:
        print(f'{lang1}')