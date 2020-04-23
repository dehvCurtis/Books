pets = {
    'Dakota': {
        'owner':'dave',
        'breed':'bloodhound',
    },
    'Owen': {
        'owner':'chris',
        'breed':'pitbull',
    }
}

for pet,info in pets.items():
    print(f'{pet.title()} is a {info["breed"].title()} owned by {info["owner"].title()}')