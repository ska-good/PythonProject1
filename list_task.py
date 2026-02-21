# Задача 3.3
#
#
# backpack = ['палатка', 'спальник', 'рюкзак', 'горелка', 'дождевик', 'фонарик', 'карта', 'компас', 'спички', 'горелка', 'телевизор', 'фонарик']

# Задание 1.1
#
# print(backpack)
# backpack[6] = 'навигатор'
# print(backpack)

# # Задание 1.2
#
# backpack.append('веревка')
# print(backpack)
#
# # Задание 1.3
#
# backpack = backpack[::-1]
# print(backpack)
#
# backpack.reverse()
# print(backpack)

# # Задание 1.4
#
# backpack.remove('телевизор')
# print(backpack)
#
# # Задание 1.5
#
# digit = len(backpack)
# digit = int(12/2)
# print(digit)
# backpack[6] = 'бутылка'
# print(backpack)
#
# # Задание 1.6
#
# backpack.count('фонарик')
# print("количество фонариков", backpack.count('фонарик'))
# backpack.count('горелка')
# print("количество горелок",backpack.count('горелка'))
#
# # Задание 1.7
#
# print(len(backpack))
#
# # Задание 1.8

# print(backpack)
# backpack.pop()
# print(backpack)

# Задание 1.9
#
# backpack_2 = backpack[:]
# print(backpack)
# print(backpack_2)
# backpack_2.append('кальян')
# print(backpack)
# print(backpack_2)
# backpack_2.remove('кальян')
# print(backpack)
# print(backpack_2)

# Задание 1.10

# duplicates_backpack = []
# unique_items = []
#
# for item in backpack:
#     if item in unique_items:
#         duplicates_backpack.append(item)
#     else:
#         unique_items.append(item)
# backpack = unique_items
#
# print("Основной рюкзак (без дубликатов):", backpack)
# print("Рюкзак с дубликатами:", duplicates_backpack)

# Задание 1.11

# backpack.sort(reverse=True)
# print("Рюкзак после сортировки:", backpack)
# backpack_2 = []
# items_5 = backpack[:5]
# print("Предметы для перемещения:", items_5)
#
# for item in items_5:
#     backpack.remove(item)
#     backpack_2.append(item)
# print("Первый рюкзак:", backpack)
# print("Второй рюкзак:", backpack_2)

# Задание 2.1

# backpack = ['фонарик', 'горелка', 'фонарик', 'спички', 'спальник', 'рюкзак', 'навигатор']
# backpack_2 = []
#
# for item in backpack:
#     backpack_2.append(len(item))
#
# print(backpack)
# print(backpack_2)

# Задание 2.2

# backpack = ['фонарик', 'горелка', 'фонарик', 'спички', 'спальник', 'рюкзак', 'навигатор']
# backpack_2 = []
#
# for item in backpack:
#     if len(item) % 2 == 0:
#         backpack_2.append(item)
#
# print(backpack)
# print(backpack_2)

# Задание 2.3

# backpack = ['фонарик', 'горелка', 'фонарик', 'спички', 'спальник', 'рюкзак', 'навигатор']
#
# for item in backpack:
#     for i in range(7):
#         print(f"{i} : {backpack[i]}")
#     break

# Задание 2.4

# backpack = ['фонарик', 'горелка', 'фонарик', 'спички', 'спальник', 'рюкзак', 'навигатор']
# backpack_2 = []
#
# for item in backpack:
#     item = item[::-1]
#     backpack_2.append(item)
# backpack = backpack_2
# print(backpack)

# Задание 2.5

# backpack = ['фонарик', 'горелка', 'фонарик', 'спички', 'спальник', 'рюкзак', 'навигатор']
# backpack_2 = []
#
# for item in backpack:
#     item = item[:1:]
#     backpack_2.append(item)
# backpack = backpack_2
#
# print(backpack)