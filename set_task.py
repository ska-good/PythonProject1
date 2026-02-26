# Задача 4.2

# Задание 1.1

# europe_set = {"Франция", "Сербия", "Андорра", "Норвегия", "Португалия", "Бельгия"}
#
# europe_set.add("Исландия")
# print(europe_set)

# Задание 1.2

# asia_set = {"Япония", "Лаос", "Шри-Ланка", "Китай", "Филиппины", "Камбоджа"}

# asia_set.discard("Япония")
# print(asia_set)
# asia_set.discard("Вьетнам") # удалит если есть, если нет - ошибку не выдаст
# asia_set.remove("Вьетнам") # удалит если есть, если нет - ошибку выдаст

# Задание 1.3

# europe_set = {"Франция", "Сербия", "Андорра", "Норвегия", "Португалия", "Бельгия"}
#
# europe_set.add("Испания")
# europe_set.add("Греция")
# europe_set.add("Норвегия")
# print(europe_set)

# Задание 1.4

# europe_set = {"Франция", "Сербия", "Андорра", "Норвегия", "Португалия", "Бельгия"}

# pop_countries = europe_set.pop()
# print(pop_countries)
# print(europe_set)

# Задание 1.5
#
# countries = set()
# countries.add("Китай")
# countries.add("Япония")
# countries.add("Тайланд")
# countries.add("Испания")
# countries.add("Черногория")
# print(countries)
#
# # Задание 1.6
#
# countries.clear()
# print(countries)

# Задание 2.1

# visited = {"Италия", "Франция"}
# wishlist = {"Франция", "Япония", "Норвегия"}
#
# print(wishlist - visited)

# Задание 2.2

# visited = {"Италия", "Франция"}
# wishlist = {"Франция", "Япония", "Норвегия"}
#
# print(visited & wishlist)

# Задание 2.3

# european_cities = {"Париж", "Берлин"}
# asian_cities = {"Токио", "Сеул"}
#
# print(european_cities.union(asian_cities))

# Задание 2.4

# eco = {"Грузия", "Норвегия"}
# cheap = {"Грузия", "Армения"}
#
# print(eco.intersection(cheap))

# Задание 2.5

# winter = {"Норвегия"}
# wishlist = {"Франция", "Япония", "Норвегия"}
#
# print(winter <= wishlist)

# Задание 2.6

# summer = {"Италия", "Испания"}
# winter = {"Норвегия"}
# summer.pop()
# print(winter.symmetric_difference(summer))

# Задание 2.7

# asian_cities = {"Токио", "Сеул"}
# x = "Сеул"
#
# print(x in asian_cities)

# Задание 2.8

# eco = {"Грузия", "Норвегия"}
# cheap = {"Грузия", "Армения"}
#
# print(eco.intersection(cheap))

# Задание 2.9

# not_interested = {"Вьетнам", "Гренландия"}
# invited_by_friends = {"Гренландия", "Исландия"}
#
# print(invited_by_friends.difference(not_interested))

# Задание 2.10

# invited_by_friends = {"Гренландия", "Исландия"}
# winter = {"Норвегия"}
#
# print(invited_by_friends >= winter)