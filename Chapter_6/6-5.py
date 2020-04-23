rivers = {
    "amazon":"brazil",
    "nile":"egypt",
    "parana":"brazil",
}

# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for k,v in rivers.items():
    print(f'The {k.title()} river runs through {v.title()}')

# Use a loop to print the name of each river included in the dictionary.
for name in rivers.keys():
    print(f'Name: {name.title()}')

# Use a loop to print the name of each country included in the dictionary.
for country in rivers.values():
    print(f'Country: {country.title()}')