fav_places = {
    "Antwerp" : {
        "country":"belgium",
        "continent":"europe",
    },
    "Paris" : {
        "country": "france",
        "continent": "europe",
    },
    "Utah" : {
        "country":"usa",
        "continent":"north america",
    }
}

for place,info in fav_places.items():
    print(f'The city of {place.title()} is in {info["country"].title()} and on the continent of {info["continent"].title()}')