# Задача 5.1

# Задание 1

# salt = "морская"
# def cook_pasta(salt = "поваренная"):
#     print(salt)
# print(salt)
# cook_pasta()

# Задание 2

# pepper = "чёрный"
# def change_pepper():
#     pepper = "красный"
#     print(pepper)
# print(pepper)
# change_pepper()

# Задание 3

# pepper = "чёрный"
# def change_pepper():
#     global pepper
#     pepper = "красный"
# change_pepper()
# print(pepper)

# Задание 4

# oil = "оливковое"
# def cook_salad():
#     oil = "подсолнечное"
#     print(oil)
# print(oil)
# cook_salad()

# Задание 5

# eggs = 10
# def use_eggs():
#     eggs -= 1
#     print(eggs)
# print(eggs)
# use_eggs()

# Задание 6

# eggs = 10
# def use_eggs():
#     global eggs
#     eggs -= 1
#     print(eggs)
# print(eggs)
# use_eggs()

# Задание 7

# def make_marinade():
#     sauce = "кисло-сладкий"
#     print(sauce)
#     def add_secret_ingredient():
#         sauce = "соевый"
#         print(sauce)
#     add_secret_ingredient()
#
# make_marinade()

# Задание 8

# def make_marinade():
#     sauce = "кисло-сладкий"
#     def add_secret_ingredient():
#         nonlocal sauce
#         sauce = "соевый"
#     add_secret_ingredient()
#     print(sauce)
# make_marinade()

# Задание 9

# def main_recipe():
#     spice = "карри"
#     print(spice)
#     def step():
#         print(spice)
#         def detail_step():
#             nonlocal spice
#             spice = "паприка"
#         detail_step()
#         print(spice)
#     step()
# main_recipe()

# Задание 10

# def recipe():
#     def inner():
#         nonlocal new_ing
#         new_ing = "шоколад"
#         print(new_ing)
#     inner()
# recipe()
# произойдет ошибка

# Задание 11

# def prepare():
#     main_ing = "томат"
#     spice = "базилик"
#     print(spice)
#     print(main_ing)
#     def adjust():
#         nonlocal spice
#         spice = "орегано"
#         print(spice)
#     adjust()
# prepare()

# Задание 12

# def pantry():
#     stock = {"sugar": 5}
#     print(stock)
#     def update_stock():
#         nonlocal stock
#         stock["sugar"] += 1
#         print(stock)
#     update_stock()
#     print(stock)
# pantry()

# Задание 13

# flour = "пшеничная"
# def bake_cake():
#     flour = "кукурузная"
#     print(flour)
#     def step():
#         print(flour)
#     step()
# bake_cake()
# print(flour)

# Задание 14

# def make_dough():
#     yeast = "сухие"
#     print(yeast)
#     def activate_yeast():
#         yeast = "живые"
#         print(yeast)
#     activate_yeast()
# make_dough()

# Задание 15

# sugar = 100
#
# def bake():
#     sugar += 1
#     print(sugar)
# bake()
# print(sugar)
#  произойдет ошибка

# Задание 16

# spice = "паприка"
# def outer():
#     spice = "карри"
#     def inner():
#         print(spice)
#     inner()
# outer()
