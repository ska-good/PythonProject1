# Задача 3.1
#
# Задание 1.1

# radius = 5
# height = 10
# pi = 3.14159
# var = pi*(radius**2)*height
# print("radius =", radius)
# print("height =", height)
# print("pi =", pi)
# print("Объем цилиндра:",f"{var:.2f}")

# Задание 1.2

# temp_C = 36.6
# temp_F=(temp_C*9/5)+32
# print("temp_F:",f"{temp_F:.2f}")
# print("temp_С:",f"{temp_C:.1f}")

# Задание 1.3
#
# distance = 185
# time = 3
# speed = distance/time

# print("distance:",f"{distance}")
# print("time:", time)
# print("speed:",f"{speed:.2f}")

# Задание 2.1
#
# s1 = "111" * 5
# print(s1)
# s2 =  111 * 5
# print(s2)
# s3 = 111.11 * 5
# print(s3)
# s4 = "111" * "111"
# print(s4)

# Задание 2.2
#
#
# new_str = "BOdHnKEWDpTFVgqdCkMVZTaQzXQBDjdiufEX"
#
# if new_str.isalpha():
#     print(f"Строка {new_str} содержит только буквы")
# elif new_str.isdigit():
#     print(f"Строка {new_str} содержит только цифры")

# Задание 2.3

# sentence = "Learning Python is fun and useful"
# words = len(sentence.split(" "))
# print(f"кол-во слов в строке = {words}")

# Задание 2.4
#
# sentence = "Learning Python is fun and useful"
# words = sentence.split(" ")
#
# # words = ['Learning', 'Python', 'is', 'fun', 'and', 'useful']
#
# m = "-".join(words)
# print("слова через '-':", f"{m}")

# # Задание 3.1
#
# backpack1 = "         	пАлатка, спаЛьник, рЮКзак           	"
# backpack2 = " горЕЛка!фОнарик!карта!компАС"
# backpack3 = " икЧИпс"
#
# backpack1 = backpack1.strip()
# print(backpack1)
#
# # Задание 3.2
#
# backpack2 = backpack2.replace("!", ", ")
#
# print(backpack2)
#
# # Задание 3.3
#
# print(id(backpack3))
#
# backpack3 = backpack3[::-1]
# print(backpack3)
# print(id(backpack3))
#
# # Задание 3.4
#
# backpack1 = backpack1.lower()
# print(backpack1)
#
# # Задание 3.5
#
# print(len(backpack2))
# backpack2 = backpack2[0:18:1]
# print(backpack2)
# backpack3 = backpack2 + backpack3
# print(backpack3)
#
# # Задание 3.6
#
# backpack3 = backpack3 * 3
# print(backpack3)
#
# # Задание 3.7
#
# print(id(backpack1))
# backpack1 = backpack1 + backpack2 + backpack3
# print(id(backpack1))
# print(backpack1)
#
# # Задание 3.8
#
# backpack1 = backpack1.title()
# print(backpack1)
#
# # Задание 3.9
#
# print(backpack1.find("Карта"))
#
# # Задание 3.10
#
# print("длина строки =", len(f"{backpack1}"))
#
# # Задание 3.11
#
# print(backpack1)
# backpack1 = backpack1.replace("  ", " ")
# print(backpack1)
# backpack1 = backpack1.replace(" ", ",")
# print(backpack1)
# backpack1 = backpack1.replace(",,", ",")
# print(backpack1)
# backpack1 = backpack1.replace(",", ", ")
# print(backpack1)