# Задача 4.4

# Задание 1.1

# def daily_reminder():
#     print("Не забудь выпить воду и сделать растяжку сегодня!")
# daily_reminder()

# Задание 1.2

# def log_sleep(quantity):
#     print(f"Количество часов сна: {quantity}")
# log_sleep(10)

# Задание 1.3

# def calculate_water_intake(weight, age):
#     if age < 30:
#         water_ml = weight * 40
#     elif 30 <= age <= 55:
#         water_ml = weight * 35
#     else:  # age > 55
#         water_ml = weight * 30
#
#     water_liters = round(water_ml / 1000, 2)
#
#     return water_liters
# weight1 = 70
# age1 = 25
# result1 = calculate_water_intake(weight1, age1)
# print(f"Возраст: {age1} лет (< 30)")
# print(f"Вес: {weight1} кг")
# print(f"Формула: {weight1} × 40 мл = {weight1 * 40} мл")
# print(f"Рекомендуемое количество воды: {result1} л")

# Задание 1.4

# def track_mood(mood="хорошее", energy=7):
#     print(f"Ваше настроение: {mood}. Уровень энергии: {energy}/10.")
# track_mood("отличное", 10)

# Задание 1.5

# def list_healthy_habits(*items):
#     print("Полезные привычки:")
#     for item in items:
#         print(f"-{item}")
#
# list_healthy_habits("Привычка1", "Привычка2", "Привычка3")

# Задание 1.6

# def health_summary(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# health_summary(sleep = "7 hours", water = "2 liters", steps = 8000)

# Задание 1.7

# def bmi(weight: float, height: float) -> float:
#     return weight / (height ** 2)
#
# result = bmi(70, 1.75)
# print(f"Ваш BMI: {result:.2f}")
#
# # Дополнительные примеры вызовов
# print(f"BMI для человека 80 кг и 1.80 м: {bmi(80, 1.80):.2f}")
# print(f"BMI для человека 55 кг и 1.65 м: {bmi(55, 1.65):.2f}")

# Задание 2.1

# def movie_night_reminder():
#     print("Не забудь устроить себе вечер кино!")
# movie_night_reminder()

# Задание 2.2

# def print_movie_rating(movie, rating):
#     print(f"Фильм {movie} получил оценку {rating}/10.")
# print_movie_rating("Форсаж", 9)

# Задание 2.3

# def calculate_watch_time(episodes, duration):
#     munites = duration * episodes
#     print(f"Общее время просмотра: {munites} минут")
# calculate_watch_time(10, 50)

# Задание 2.4

# def plan_movie_session(movie="Inception", snack="попкорн"):
#     print(f"Фильм на сегодня: {movie}, а закуска к фильму: {snack}." )
# plan_movie_session()
#
# Задание 2.5

# def list_favorite_movies(*items):
#     print("Любимые фильмы:")
#     for item in items:
#         print(f"-{item}")
#
# list_favorite_movies("Форсаж", "Титаник", "Кинг Конг", "Джентельмены")

# Задание 2.6

# def prepare_movie_night(snack="попкорн", *movies):
#     print( f"Ты выбрал закуску: {snack}")
#     if len(movies) > 0:
#         print("Список выбранных фильмов:")
#         for movie in movies:
#             print(f"-{movie}")
#     else:
#         print("Фильмы пока не выбраны.")
# prepare_movie_night( "чипсы", "Фильм1","Фильм2", "Фильм3", "Фильм4")
# # prepare_movie_night()

# Задание 2.7

# def series_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# series_info(title = "Breaking Badn", seasons = 5, genre = "Crime, Drama")

# Задание 2.8

# def average_episode_duration(episode: float, duration: float) -> float:
#     average = duration / episode
#     print(f"Средняя продолжительность одной серии = {average} минут")
# average_episode_duration(10, 100)

# Задание 2.9

# def plan_movie_session(movie="Inception", snack="попкорн"):
#     print(f"Фильм на сегодня: {movie}, а закуска к фильму: {snack}." )
#
# def movie_night_reminder():
#     print("Не забудь устроить себе вечер кино!")
#
# def movie_marathon_plan():
#     movie_night_reminder()
#     plan_movie_session("Кинг Конг", "чипсы")
#
# movie_marathon_plan()