fav_places = {
    "Devon" : {
        "country":"belgium",
        "restaurant":"mcdonalds",
    },
    "Molly" : {
        "country": "france",
        "restaurant": "taco bell",
    },
    "Brandon" : {
        "country": "usa",
        "restaurant": "arby's",
    }
}

for name,info in fav_places.items():
    print(f'{name.title()}\'s favorite place to visit is {info["country"].title()} while eating {info["restaurant"].title()}')