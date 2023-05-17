travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

def add_new_country(name, visit_count, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["total_visits"] = visit_count
    new_country["cities"] = cities_visited    
    travel_log.append(new_country)
    
add_new_country("Ukraine", 3, ["Kiev", "Cherkassy"])
print(travel_log)