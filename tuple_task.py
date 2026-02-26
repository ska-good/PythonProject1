# Задача 4.1
from operator import index, countOf

# Задание 1.1

# cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
#
# landmarks = ("Лувр", "Колизей", "Бундестаг", "Биг Бен", "Кремль")
#
# for i, citi in enumerate(cities):
#     print(f"{i}. {citi}")

# Задание 1.2

# cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
#
# for item in cities:
#     for i in range(5):
#         print(f"{i} : {cities[i]}")
#     break

# Задание 1.3

# cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
# print(cities[::-1])

# # Задание 1.4
#
# cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
# print(cities[1:4:])

# Задание 1.5
#
# cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
# print(cities[1::2])

# Задание 1.6
#
# landmarks = ("Лувр", "Колизей", "Бундестаг", "Биг Бен", "Кремль")
# for x in landmarks:
#     if x.startswith("Б"):
#         print(x)

# Задание 1.7
#
# cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
# start_index = cities.index("Берлин")
#
# print(cities[start_index::])

# Задание 1.8

# cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
# c = ()
# for x in cities:
#     c = c + (f"{x}",)*2
# print(c)

# Задание 1.9

# cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
#
# index = 0
# while index < 3 < len(cities):
#     x = cities[index] + '!'
#     print(x)
#     index += 1

# Задание 1.10

# cities = ("Париж", "Рим", "Берлин", "Лондон", "Москва")
# print(cities)
# print(id(cities))
# cities = cities + ("Самара", "Омск",)
# print(cities)
# print(id(cities))

# Задание 2.1

# visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
# city = set(visited)
#
# for x in city:
#     count = visited.count(x)
#     print(f"{x}: {count}")


# Задание 2.2

# visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
#
# print(visited.index("Вена"))

# Задание 2.3

# countries = ("Франция", "Италия", "Франция", "Австрия", "Германия", "Германия")
#
# if "Амстердам" in countries:
#     print("Турист был в Амстердаме")
# else:
#     print("Турист не был в Амстердаме")

# Задание 2.4

# visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
# k = 0
# city = ""
#
# for c in set(visited):
#     count = visited.count(c)
#     if count > k:
#         k = count
#         city = c
# print(f"Город посещён чаще других: {city} - {k} раза")


# Задание 2.5

# visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
# x = []
#
# for city in visited:
#     if visited.count(city) == 1:
#         x.append(city)
#         print(x)

# Задание 2.6

# countries = ("Франция", "Италия", "Франция", "Австрия", "Германия", "Германия")
#
# countries = set(countries)
# print(len(countries))

# Задание 2.7

# visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
#
# index = 0
# while index < len(visited):
#     if visited[index] == "Париж":
#         print(index)
#     index += 1

# Задание 2.8

# visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
#
# if visited.count("Вена") > visited.count("Рим"):
#     print("В Вене турист был  больше, чем в Риме, он был там раза", visited.count("Вена"))
# elif visited.count("Вена") < visited.count("Рим"):
#     print("В Риме турист был  больше, чем в Вене, он был там раза", visited.count("Рим") )

# Задание 2.9

# visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
# city = set(visited)
#
# for x in city:
#     count = visited.count(x)
#     if count > 1:
#         print(f"{x}: {count}")

# Задание 2.10

# visited = ("Рим", "Париж", "Рим", "Вена", "Париж", "Рим")
# print(visited.index("Вена", 2,4))

# # Задание 2.11
#
# eurotrip = ("Минск", "Варшава", "Будапешт", ["Загреб", "Зальцбург", "Вена"], "Мюнхен")
# print(id(eurotrip))
# eurotrip[3][1] = "Любляна"
# print(eurotrip)
# print(id(eurotrip))