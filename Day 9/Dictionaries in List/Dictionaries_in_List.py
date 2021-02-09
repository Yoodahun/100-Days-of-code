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


# 🚨 Do NOT change the code above


# to be added to the travel_log. 👇
def add_new_country(contry_name, visit_time, cities):
    add_country_info = {
        "country": contry_name,
        "visits": visit_time,
        "cities": cities
    }
    travel_log.append(add_country_info)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
