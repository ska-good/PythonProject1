# Задача 2.4
#
# Задание 1.1
#
# print("Введите число")
# x = input()
# x = int(x)
# if x < 0:
#     print("Отрицательное")
# elif x > 0:
#     print("Положительное или ноль")
#
# print("Введите число")
# x = input()
# x = int(x)
# if x % 2 == 0:
#     print("Четное")
# elif x % 2 != 0:
#     print("Нечетное")
#
# print("Введите число")
# x = input()
# x = int(x)
# if x > 100:
#     print("Число слишком большое")
# else: print("Число подходит")

# Задание 1.2

# print("Введите время записи")
# x = input()
# x = int(x)
#
# y = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
# if x in y:
#     print("Вы записаны")
# else: print("Ошибка! Вы выбрали нерабочее время")
#
# Задание 2.1

# print("Введите число")
# x = input()
# x = int(x)
#
#
# if -100 < x < 100:
#     if x > 0:
#         print("Положительное")
#     elif x < 0:
#         print("Отрицательное")
#     else:
#         print("Ноль")
# else:
#     print("Ошибка")

# Задание 2.2

# print("Введите ваш возраст: ")
# age = input()
# age = int(age)
#
# if age <= 0:
#     print("Ошибка")
# elif age < 18:
#     print("Несовершеннолетний")
# elif 18 <= age <= 59:
#     print("Взрослый")
# else:
#     print("Пенсионер")

# Задание 2.3

# print("Введите оценку (целое число от 1 до 5): ")
# x = input()
#
# if x == '5':
#     print("Отлично")
# elif x == '4':
#     print("Хорошо")
# elif x == '3':
#     print("Удовлетворительно")
# elif x == '2':
#     print("Плохо")
# elif x == '1':
#     print("Очень плохо")
# else:
#     print("Недопустимая оценка")

# Задание 2.4

# try:
#     age = int(input("Введите ваш возраст: "))
# # except ValueError:
# #     # Если введено не целое число
# #     print("Ошибка")
# #     exit()
#
# if age <= 0:
#     print("Ошибка")
# elif age < 23:
#     print("Ваша студенческая скидка 20%")
# elif age <= 60:
#     print("Скидка не предусмотрена")
# else:
#     print("Ваша пенсионная скидка 30%")

    # Задание 2.5

milk_list_available = ["burenka", "prostokvashino", "vkusnoteevo", "happy cow"]
milk_list_not_available = ["domik v derevne", "nasha korova"]

milk_order = input("Какое молоко вы хотите заказать? ")

if milk_order in milk_list_available:
    print("Заказ принят!")
elif milk_order in milk_list_not_available:
    print("К сожалению, данный продукт закончился")
else:
    print("Мы не продаем данную продукцию")