# Задача 5.4

# Задание 1.1

# def wrap_food(input_function):
#     def out_food(meal):
#         print(f"Готовим: {meal}")
#         return input_function(meal)
#     return out_food
#
#
# @wrap_food
# def food(meal):
#     print(f"{meal} готово!")
#
# food("яйцо")

# Задание 1.2

# def repeat(func):
#     def wrapper(n, meal):
#         for i in range(1, n + 1):
#             print(f"{meal}: порция {i}")
#         return func(n, meal)
#     return wrapper
#
# @repeat
# def serve_meal(n, meal):
#     print(f"{meal} подано")
#
# serve_meal(20, "цезарь‑салат")

# Задание 1.3

# def log_ingredients(func):
#     def wrapper(meal, **ingredients):
#         print(f"Ингредиенты для '{meal}':")
#         for ingredient, amount in ingredients.items():
#             print(f"  - {ingredient}: {amount}")
#         return func(meal, **ingredients)
#     return wrapper
#
# @log_ingredients
# def cook_meal(meal, **ingredients):
#     print(f"{meal} готово!")
#
# cook_meal("Греческий салат", томаты="2 шт", огурцы="1 шт", сыр="100 г", масло="1 ст.л")

# Задание 1.4

# def validate_positive(func):
#     def mat(ves, min):
#         if ves <= 0  or min <= 0:
#             print("Неверные данные")
#             return None
#         return func(ves, min)
#     return mat
#
# @validate_positive
# def mop(ves, min):
#     print(f"Мариновать {ves}г мяса {min} мин.")
# mop(1000, 20)

# Задание 1.5

# def calculate_total_cost(func):
#     def wrapper(*prices):
#         total = sum(prices)
#         print(f"Общая стоимость ингредиентов: {total:.2f} руб.")
#         return func(*prices)
#     return wrapper
#
#
# @calculate_total_cost
# def show_ingredients_count(*prices):
#     count = len(prices)
#     print(f"Куплено ингредиентов: {count} шт.")
#     if count > 0:
#         print(f"Средняя стоимость: {sum(prices) / count:.2f} руб.")
#
# print("Обед из 3 ингредиентов:")
# show_ingredients_count(150.50, 230.00, 89.90)

# Задание 2.1

# def filter_by_rating(threshold):
#     # Декоратор, который фильтрует фильмы по минимальной оценке
#     #     threshold: минимальный рейтинг для фильтрации
#     def decorator(func):
#         def wrapper(film_ratings):
#             # Фильтруем фильмы: оставляем только те, у которых рейтинг >= threshold
#             filtered_films = {
#                 title: rating
#                 for title, rating in film_ratings.items()
#                 if rating >= threshold
#             }
#             # Вызываем исходную функцию с отфильтрованным словарём
#             return func(filtered_films)
#         return wrapper
#     return decorator
#
# @filter_by_rating(threshold=8)
# def display_films(films):
#     # Выводит список отфильтрованных фильмов
#     film_list = ", ".join(films.keys())
#     print(f"Отфильтрованные фильмы: {film_list}")
#
# film_ratings = {
#     "Дюна": 9,
#     "Матрица": 10,
#     "Начало": 7,
#     "Крёстный отец": 9,
#     "Ёлки 5": 5
# }
# display_films(film_ratings)

# Задание 2.2

# def average_duration_decorator(func):
#     # Декоратор, который вычисляет и выводит среднюю длительность фильмов
#     def wrapper(films):
#         # Вычисляем среднюю длительность
#         total_duration = sum(films.values())
#         film_count = len(films)
#         average = total_duration / film_count if film_count > 0 else 0
#         print(f"Средняя длительность фильмов: {average:.1f} минут")
#         # Вызываем исходную функцию
#         return func(films)
#     return wrapper
#
# @average_duration_decorator
# def display_film_durations(films):
#     # Отображает информацию о длительности фильмов
#     for title, duration in films.items():
#         hours = duration // 60
#         minutes = duration % 60
#         print(f"   {title}: {duration} минут ({hours}ч {minutes}мин)")
#     print("Длительность фильмов посчитана")
#
# durations = {"Дюна": 155, "Матрица": 136, "Начало": 148}
#
# display_film_durations(durations)

# Задание 2.3

# import random
#
# def discount_decorator(func):
#     # Декоратор, который добавляет случайную скидку на закуски
#     def wrapper(prices):
#         # Вычисляем общую стоимость
#         total_cost = sum(prices)
#         # Генерируем случайную скидку (от 50 до 200 рублей)
#         discount = random.randint(50, 200)
#         # Применяем скидку
#         final_cost = total_cost - discount
#         # Если скидка больше стоимости, то итоговая стоимость не может быть отрицательной
#         if final_cost < 0:
#             final_cost = 0
#         # Выводим информацию о скидке
#         print(f"Скидка: {discount} руб, Итого: {final_cost} руб")
#         # Вызываем исходную функцию
#         return func(prices)
#     return wrapper
#
# @discount_decorator
# def display_snacks(prices):
#     # Отображает количество купленных закусок
#     print(f"Количество купленных закусок: {len(prices)}")
# # Вызов функции с несколькими ценами
# snack_prices = [150, 80, 200, 120, 90]
# display_snacks(snack_prices)

# Задание 2.4

# def time_validator_decorator(func):
#     # Декоратор, который проверяет корректность времени сеанса
#     def wrapper(film, hour):
#         # Проверяем, входит ли время в допустимый диапазон (8:00 - 23:00)
#         if 8 <= hour <= 23:
#             # Если время корректное, вызываем функцию
#             return func(film, hour)
#         else:
#             # Если время некорректное, выводим предупреждение
#             print(f"ПРЕДУПРЕЖДЕНИЕ: Время {hour}:00 не входит в допустимый диапазон (8:00-23:00)")
#             print(f" Фильм '{film}' не может быть показан в это время")
#             return None
#     return wrapper
#
# @time_validator_decorator
# def show_movie_session(film, hour):
#     # Отображает информацию о сеансе фильма
#     print(f"Фильм: {film}")
#     print(f"Начало сеанса: {hour}:00")
#     print("Сеанс успешно запланирован!")
# # Вызов функции с некорректным временем
# show_movie_session("Матрица", 2)
# show_movie_session("Дюна", 20)

# Задание 2.5

# def check_schedule_decorator(func):
#     # Декоратор, который проверяет наличие фильма в расписании
#     def wrapper(film, schedule):
#         # Проверяем, есть ли фильм в расписании
#         if film in schedule:
#             # Если фильм есть, вызываем функцию с временем из расписания
#             return func(film, schedule)
#         else:
#             # Если фильма нет, выводим предупреждение
#             print(f"ПРЕДУПРЕЖДЕНИЕ: Фильм '{film}' отсутствует в расписании!")
#             print(f"Доступные фильмы: {', '.join(schedule.keys())}")
#             return None
#     return wrapper
#
# @check_schedule_decorator
# def show_movie_time(film, schedule):
#     # Отображает информацию о начале фильма
#     time = schedule[film]
#     print(f"Фильм: {film}")
#     print(f"Начало сеанса: {time}")
#     print("Билеты доступны для покупки!")
#
# # Расписание кинотеатра
# schedule = {
#     "Дюна": "18:00",
#     "Матрица": "20:30",
#     "Интерстеллар": "23:00",
#     "Шрек 2": "16:20"
# }
# # Вызов с фильмом, которого нет в расписании
# show_movie_time("Титаник", schedule)
# show_movie_time("Дюна", schedule)