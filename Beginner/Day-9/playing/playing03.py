travel_log = {
    "Brazil": {"cities_visited": ["Campo Grande", "Dourados", "Corumba"], "total_visits": 12},
    "Estonia": {"cities_visited": ["Tallinn", "Tartu", "Parnu"], "total_visits": 1}
}
for k in travel_log:
    print(f"{k} ----> {travel_log[k]}")

travel_log2 = [
    {
        "country": "Brazil",
        "cities_visited": ["Campo Grande", "Dourados", "Corumba"],
        "total_visits": 12
    },
    {
        "country": "Estonia",
        "cities_visited": ["Tallinn", "Tartu", "Parnu"],
        "total_visits": 1
    }
]
for key in travel_log2:
    print(key)
