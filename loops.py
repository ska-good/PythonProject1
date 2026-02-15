# Задача 3.2
#
# Задание 1.1
from operator import index

# x = "Python is the best programming language"
# x = x.split(" ")
# print("x:", x)
# for y in x:
#     if 3 < len(y):
#         print("слово длинее 3 букв:", y)
#         continue

# Задание 1.2

# for r in range(15,100):
#     if r % 13 == 0:
#         print(r)
#         break

# Задание 1.3

# for x in range(1,30):
#     if x % 5 != 0:
#         print(x)
#         continue

# Задание 1.4

# for x in range(1,100):
#     for y in range(1,100):
#         if x + y == 50:
#             print(x, y)
#     break

# for x in range(1,100):
#     for y in range(1,100):
#         if x == y == 50 / 2:
#             print(x, y)
#             break

# # Задание 1.5
#
# matrix = [[(x,y) for y in range(1,4)] for x in range(1,4)]
# for row in matrix:
#     print(row)

# Задание 2.1
#
# backpack = "вереВКа, спИЧки, коМПАс, нАВигатор, фОНарик, гореЛКа, рюкзАК, спалЬник, палаткА"
# backpack = backpack.replace(",", "" )
# backpack = backpack.split()
# print(backpack)
# for items in backpack:
#     print(items)
#
# # Задание 2.2
#
# for items in backpack:
#     items = items.title()
#     print(items)

# Задание 2.3

# for items in backpack:
#     items = items[::-1]
#     print(items)

# index = 0
# while index < len(backpack):
#     items = backpack[index][::-1]
#     print(items)
#     index += 1

# Задание 2.4

# vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
# for items in backpack:
#     if items[0] in vowels:
#         print(items)

# Задание 2.5

# for items in backpack:
#     items = items.lower()
#     print(items)

# index = 0
# while index < len(backpack):
#     items = backpack[index].lower()
#     print(items)
#     index += 1
#
# Задание 2.6

# longest_word = ''
# for items in backpack:
#     if len(items) > len(longest_word):
#         longest_word = items
# print(f"Самое длинное слово: {longest_word}")

# Задание 2.7

# index = 0
# while index < len(backpack):
#     if len(backpack[index]) < 7:
#         print(backpack[index])
#     index += 1

# # Задание 2.8
#
# index = 0
# while index < len(backpack):
#     items = backpack[index] + '!'
#     print(items)
#     index += 1