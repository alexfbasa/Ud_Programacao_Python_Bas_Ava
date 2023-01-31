travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_countries(new_country, total_visits, cities_visited):
    new_countries_list = {}
    new_countries_list["country"] = new_country
    new_countries_list["visits"] = total_visits
    new_countries_list["cities"] = cities_visited
    travel_log.append(new_country)


add_new_countries('Portugal', 2, ['Lisbon', 'Porto'])

print(travel_log)
