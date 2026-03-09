# Задача 4.3

# # Задание 1.1
#
# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
#
# for item in trip["tourist"]:
#     if len(item) > 4:
#         print(item)

# # Задание 1.2
#
# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
# x = ("F", "G")
#
# for item in trip["plan"]:
#     if item[0] in x:
#         print(item)

# Задание 1.3

# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
#
# sm = trip["tourist"]
# for key, value in sm.items():
#     if isinstance(value, str):
#         if len(value) > 5:
#             print(f"{key}: {value}")


# Задание 1.4

# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
# }
#
# for i, key in enumerate(trip["plan"]):
#     print(f"{i+1}. {key}: {trip["plan"][key]}")

# Задание 1.5
#
# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
#
# trip["tourist"] = dict(sorted(trip["tourist"].items()))
# print(trip["tourist"])

# Задание 1.6
#
# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
# count = 0
#
# for key in trip["plan"]:
#     if len(trip["plan"][key]) < 6:
#         count += 1
# print(count)

# Задание 1.7

# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
#
# sm = trip["plan"]
# for values in sm.values():
#     if "e" in values:
#         print(values)

# Задание 1.8

# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
#
# x = []
# sm = trip["costs"]
# for values in sm.values():
#     if values > 100:
#         x.append(values)
# print(sum(x))

# Задание 1.9

# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
#
# sm = trip["plan"]
# result = []
#
# for key, value in sm.items():
#     if key.startswith('I') or 'a' in value:
#         result.append(f"{key} : {value}")
#
# print(result)

# Задание 1.10

# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
#
# x = trip["plan"]
# for values in x.values():
#     if values == "Rome":
#         print("есть значение 'Rome'")
#         break
#     elif values != "Rome":
#         print("нет значения 'Rome'")
#         break

# Задание 2.1

# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museum s":120}
#
# }
#
# trip_1 = trip["tourist"]
# trip_1["email"] = "anna.moreau@example.com"
# print(trip_1)

# Задание 2.2

# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
#
# trip["tourist"]["age"] += 1
# print(trip)

# Задание 2.3

# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museum s":120}
#
# }
#
# trip_1 = trip["costs"]
# x = {"transport" : 60}
# trip_1.update(x)
# print(trip_1)

# # Задание 2.4
#
# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museum s":120}
#
# }
#
# trip_1 = trip["plan"]
# trip_1.setdefault("Spain", "Barcelona")
# print(trip_1)

# Задание 2.5

# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
#
# trip_1 = trip["costs"]
# x = trip_1.pop("museums")
# print(trip_1)
# print(x)

# Задание 2.6

# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
#
# trip_1 = trip["plan"]
# key, value = trip_1.popitem()
# print(trip_1)
# print(f"удаленные {key}: {value}")
# print(trip)

# Задание 2.7

# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
#
# trip["tourist"].clear()
#
# print(trip['tourist'])
# print(f"tourist пуст? {bool(trip['tourist'])}")

# Задание 2.8

# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
#
# backup_costs = trip["costs"]
# backup_costs["hotel"] = 500
# print(trip)
# print(backup_costs)

# Задание 2.9

# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museum s":120}
#
# }
#
# trip_1 = trip["tourist"]
# trip_1.setdefault("phone", "+7-123-456-7890")
# print(trip_1)

# Задание 2.10

# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
#
# trip_1 = trip["plan"]
# x = trip_1.pop("France")
# print(trip_1)
# print(x)

# Задание 2.11

# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
#
# updated_costs = {key: round(value * 1.1, 1) for key, value in trip["costs"].items()}
#
# trip["costs"].update(updated_costs)
# print(updated_costs)
# print(trip)

# Задание 2.12
#
# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
#
# updated_plan = {key: value for key, value in trip["plan"].items() if value[0] in "D"}
#
# print(updated_plan)

# Задание 2.13

# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
#
# updated_plan = {key: value for value, key in trip["plan"].items()}
#
# print(updated_plan)

# Задание 2.14

# import copy
#
# trip = {
#
# "tourist":{"name":"Anna", "lastname":"Moreau", "country":"France", "age":32},
#
# "plan":{"Italy":"Rome", "France":"Paris", "Germany":"Berlin", "Ireland":"Dublin"},
#
# "costs":{"flight":330, "hotel":650, "meals":100, "museums":120}
#
# }
#
# trip_shallow = copy.copy(trip)
# trip_deep = copy.deepcopy(trip)
#
# trip_shallow["costs"]["hotel"] = 700
# trip_deep["costs"]["flight"] = 290

# print(trip["costs"], trip_shallow["costs"], trip_deep["costs"])

# Задание 3.1

# cities = {'Paris': 250, 'Berlin': 180, 'Rome': 200, 'Madrid': 170, 'Vienna': 190}
#
# cities_2 = {key: round(value * 0.9, 1) for key, value in cities.items()}
#
# print(cities_2)
# print(cities)

# Задание 3.2

# cities = {'Paris': 250, 'Berlin': 180, 'Rome': 200, 'Madrid': 170, 'Vienna': 190}
#
# cities_2 = {key: value for key, value in cities.items() if value <  200 }
#
# print(cities_2)
# print(cities)

# Задание 3.3

# cities = {'Paris': 250, 'Berlin': 180, 'Rome': 200, 'Madrid': 170, 'Vienna': 190}
#
# cities_2 = {key.lower(): value for key, value in cities.items()}
#
# print(cities_2)
# print(cities)

# Задание 3.4

# cities = {'Paris': 250, 'Berlin': 180, 'Rome': 200, 'Madrid': 170, 'Vienna': 190}
#
# cities_2 = {
#     length: [city for city in cities.keys() if len(city) == length]
#     for length in {len(city) for city in cities.keys()}
# }
#
# print(cities_2)

# Задание 3.5

# cities = {'Paris': 250, 'Berlin': 180, 'Rome': 200, 'Madrid': 170, 'Vienna': 190}
#
# cities_2 = {city: ("Дорого" if price > 200 else "Приемлемо") for city, price in cities.items()}
#
# print(cities_2)