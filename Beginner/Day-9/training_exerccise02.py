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


def add_new_countries(country_name, city_names, visited_time, food):
    new_countries = {}
    new_countries['country'] = country_name
    new_countries['visits'] = visited_time
    new_countries['cities'] = city_names
    travel_log.append(new_countries)


add_new_countries('Portugal', 2, ['Lisbon', 'Porto'])

print(travel_log)
