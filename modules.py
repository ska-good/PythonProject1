# Задача 5.2
import math
# Задание 1.1

# countries = ['Италия', 'Франция', 'Япония', 'Норвегия', 'Чили', 'Канада', 'Перу']
# companions = ['Анна', 'Олег', 'Ирина', 'Михаил', 'Светлана']
# places = ['Эйфелева башня', 'Колизей', 'Фудзи', 'Биг-Бен', 'Ниагарский водопад']

import random

# print(random.choice(countries))

# Задание 1.2

# print(random.randint(1, 31))

# Задание 1.3

# print(random.uniform(0.90, 0.95))

# Задание 1.4

# print(random.randint(1000, 9999))

# Задание 1.5

# print(random.choices(places, k=3))

# Задание 1.6

# print(random.sample(countries, k=3))

# Задание 1.7

# discount = random.randint(5, 30)
# print(f"скидка: {discount}%")

# Задание 1.8

# visa = random.randint(1, 100)
# print(f"Шанс получения визы: {visa}%")
# if visa >= 70:
#     print("Виза одобрена")
# elif visa < 70:
#     print("Виза отклонена")

# Задание 1.9

# print(random.choice(companions))

# Задание 1.10

# budget = random.uniform(800, 2000)
# print(round(budget, 2))

# Задание 2.1

from datetime import datetime, timedelta

# date_str = "10-04-1925"
# parsed = datetime.strptime(date_str, "%d-%m-%Y")
# print(parsed)

# Задание 2.2

# from datetime import date
# book_date = date(1925, 4, 10)
#
# # Текущая дата
# today = date.today()
#
# # Вычисляем количество полных лет
# years = today.year - book_date.year
#
# # Проверяем, был ли уже день рождения в этом году
# if (today.month, today.day) < (book_date.month, book_date.day):
#     years -= 1
#
# print(f"Книга издана: {book_date.strftime('%d.%m.%Y')}")
# print(f"Сегодня: {today.strftime('%d.%m.%Y')}")
# print(f"Книге исполнилось полных лет: {years}")

# Задание 2.3

# a = datetime.now() + timedelta(days=14)
# print(a)

# Задание 2.4

from datetime import time

# my_time = time(21, 30)
# print(my_time)

# Задание 2.5

# current_date = datetime.now()
# date_string = current_date.strftime("%d.%m.%Y")
# print(date_string)

# Задание 2.6

# book1_year = 2005
# book2_year = 2015
#
# if book2_year > book1_year:
#     print(f"Книга 2015 года новее, чем книга 2005 года")
# elif book1_year > book2_year:
#     print(f"Книга 2005 года новее, чем книга 2015 года")

# Задание 2.7

# from datetime import date
#
# book_date = date(2010, 5, 5)
#
# print(book_date)

# Задание 2.8

# my_public = datetime(2021, 2, 14, 18, 45)
# print(my_public)

# Задание 2.9

# nov = datetime.now()
# formatted = nov.strftime("%Y-%m-%d %H-%M-%S")
# print(formatted)

# Задание 2.10

# today = datetime.now()
# current_day = today.day
# days_passed = current_day - 1
#
# print(f"Сегодня: {today.strftime('%d.%m.%Y')}")
# print(f"Номер текущего дня месяца: {current_day}")
# print(f"Дней прошло с начала месяца: {days_passed}")

# Задание 3.1

# import math
#
# width = 16
# height = 9
# diagonal = math.sqrt(width**2 + height**2)
# print(round(diagonal, 2))

# Задание 3.2

# x = 267 / 20
# print(round(x))

# Задание 3.3

# x = (3 * 12)/60
# print(math.ceil(x))

# Задание 3.4

# diameter = 4
# print(math.pi * diameter)

# Задание 3.5

# import math
#
# t = 2
# interest = 100 * math.exp(-0.3 * t)
#
# print(f"Интерес зрителя через {t} часа(ов): {interest:.2f}")

# Задание 3.6

# n = 5
# print(math.factorial(n))

# Задание 3.7

# d=3.5
# l = 1000 / math.sqrt(d)
# print(round(l,2))

# Задание 3.8

# x = 50 / 7
# print(math.ceil(x))

# Задание 3.9

# x = 113/60
# print(math.floor(x))

# Задание 3.10

# import math
# from datetime import datetime, timedelta, time, date
#
# x = 137/30
# h = math.ceil(x) * 30
# a = (datetime.combine(date.today(), time(18, 0)) + timedelta(minutes=h)).time()
# print(a)

# Задание 4.1

import json

# book = {
# 	"title": "1984",
# 	"author": "George Orwell",
# 	"year": 1949,
# 	"genres": ["dystopia", "political fiction", "science fiction"],
# 	"pages": 328,
# 	"available": True,
# 	"rating": 4.7
# }
# book_str = json.dumps(book)
# print(book_str)

# Задание 4.2

# data = '''
# [
# 	{
#     	"title": "1984",
#     	"author": "George Orwell",
#     	"year": 1949,
#     	"genres": ["dystopia", "political fiction"]
# 	},
# 	{
#     	"title": "Brave New World",
#     	"author": "Aldous Huxley",
#     	"year": 1932,
#     	"genres": ["dystopia", "science fiction"]
# 	},
# 	{
#     	"title": "Fahrenheit 451",
#     	"author": "Ray Bradbury",
#     	"year": 1953,
#     	"genres": ["dystopia", "speculative fiction"]
# 	}
# ]
# '''
#
# books = json.loads(data)
# print(f"Автор - {books[0]['author']}")

# Задание 4.3

# library = {
# 	"library_name": "Central Library",
# 	"location": "Main Street, 10",
# 	"books": [
#     	{"title": "1984", "author": "George Orwell", "available": True},
#     	{"title": "Brave New World", "author": "Aldous Huxley", "available": False},
#     	{"title": "Fahrenheit 451", "author": "Ray Bradbury", "available": True}
# 	]
# }
# library_str = json.dumps(library)
# print(library_str)

# Задание 4.4

# json_data = '''
# [
# 	{"title": "1984", "author": "George Orwell", "available": true},
# 	{"title": "Brave New World", "author": "Aldous Huxley", "available": false},
# 	{"title": "Fahrenheit 451", "author": "Ray Bradbury", "available": true}
# ]
# '''
#
# books = json.loads(json_data)
# for book in books:
#     if book["available"]:
#         print(f"- {book['title']}")