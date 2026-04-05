# Задача 5.5

# Задание 1.1

# def task_1(total_pages, days):
#     try:
#         print("Попытка деления...")
#         print(f"Делим {total_pages} на {days}")
#         result = total_pages / days
#     except ZeroDivisionError:
#         print("Ошибка - деление на ноль")
#     else:
#         print(f"Успешно! Результат = {result}")
#     finally:
#         print("Завершении расчёта")
# task_1(10, 2)
# task_1(10, 0)
# task_1(0, 20)

# Задание 1.2

# def task_2(books, ind):
#     try:
#         print("Попытка поиска книги...")
#         result = books[ind]
#     except IndexError:
#         print("Ошибка - нет такого индекса")
#     else:
#         print(f"Успешно! Результат = {result}")
#     finally:
#         print("Завершении поиска")
#
#
# books = [
#     "Гордость и предубеждение",
#     "Мастер и Маргарита",
#     "Три товарища",
#     "Сто лет одиночества",
#     "Унесённые ветром",
#     "Тень горы",
#     "Цветы для Элджернона",
#     "О дивный новый мир",
#     "Норвежский лес",
#     "Имя розы",
# ]
#
# task_2(books, ind=15)
# task_2(books, ind=5)

# Задание 1.3

# def task_3(books, ind):
#     try:
#         print("Попытка преобразования...")
#         result = books[ind]
#         number = int(result)
#         print(f"Преобразование успешно! Книга '{result}' → число {number}")
#     except IndexError:
#         print(f"Ошибка: Индекс {ind} выходит за границы списка (0-{len(books) - 1})")
#     except ValueError:
#         print(f"Ошибка: Невозможно преобразовать '{result}' в число")
#     else:
#         print(f"Успешно! Результат = {number}")
#     finally:
#         print("Завершении преобразования")
#
# books = [
#     "Гордость и предубеждение",
#     "Мастер и Маргарита",
#     "Три товарища",
#     "Сто лет одиночества",
#     "Унесённые ветром",
#     "Тень горы",
#     "Цветы для Элджернона",
#     "О дивный новый мир",
#     "Норвежский лес",
#     "Имя розы",
# ]
#
# task_3(books, ind=10)
# task_3(books, ind=1)

# Задание 1.4

# def task_4(books, days):
#     try:
#         print("Попытка сложения...")
#         print(f"Сумма {books} и {days}")
#         result = books + days
#     except ZeroDivisionError:
#         print("Ошибка - деление на ноль")
#     except ValueError:
#         print(f"Ошибка: Невозможно преобразовать '{result}' в число")
#     except TypeError:
#         print("Ошибка - неверный тип данных")
#     except NameError:
#         print("Ошибка - нет такой переменной")
#     else:
#         print(f"Успешно! Результат = {result}")
#     finally:
#         print("Завершении расчёта")
# task_4(10, 8)

# Задание 1.5

# catalog = {
#     "Джейн Остин": "Гордость и предубеждение",
#     "Михаил Булгаков": "Мастер и Маргарита",
#     "Эрих Мария Ремарк": "Три товарища",
#     "Габриэль Гарсиа Маркес": "Сто лет одиночества",
#     "Умберто Эко": "Имя розы",
# }
#
# def task_5(catalog, author):
#     try:
#         print("Попытка найти книгу...")
#         result = catalog[author]
#     except TypeError:
#         print("Ошибка - неверный тип данных")
#     except KeyError:
#         print("Ошибка - нет такого ключа")
#     else:
#         print(f"Успешно! Результат = {result}")
#     finally:
#         print("Завершении поиска")
# task_5(catalog, author = 'Михаил Булгаков')
# task_5(catalog, author = 'Сергей Довлатов')

# Задание 1.6

# def task_6():
#     try:
#         print("Попытка найти переменную")
#         print(penalty_rate)
#     except NameError:
#         print("Ошибка - нет такой переменной")
#     except TypeError:
#         print("Ошибка - неверный тип данных")
#     finally:
#         print("Завершении поиска")
# task_6()

# Задание 1.7

# def task_7():
#     try:
#         import recommendations_engine
#         print("Модуль recommendations_engine успешно импортирован")
#     except ModuleNotFoundError:
#         print("Ошибка: модуль 'recommendations_engine' не найден")
#         print("Пожалуйста, установите модуль или проверьте его наличие")
#
# task_7()

# Задание 1.8

# def task_8(books, book_idx_str, mult):
#     try:
#         idx = int(book_idx_str)
#         if idx < 0 or idx >= len(books):
#             raise IndexError(f"Индекс {idx} вне диапазона (0-{len(books) - 1})")
#         book = books[idx]
#         result = idx * mult
#         print("РЕЗУЛЬТАТ ВЫПОЛНЕНИЯ")
#         print(f"Список книг: {books}")
#         print(f"Индекс (строка): '{book_idx_str}'")
#         print(f"Индекс (число): {idx}")
#         print(f"Книга: {book}")
#         print(f"Вычисление: {idx} × {mult} = {result}")
#         return result
#     except ValueError:
#         print(f"Ошибка: '{book_idx_str}' не является корректным числом")
#         return None
#     except IndexError as e:
#         print(f"Ошибка: {e}")
#         return None
#     except Exception as e:
#         print(f"Неожиданная ошибка: {e}")
#         return None
# books_list = ["1984", "Brave New World", "Fahrenheit 451"]
# task_8(books_list, "1", 10)