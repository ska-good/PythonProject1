# Задача 2.2

# Задание 2

my_list = [1, 2, 3, 4, 5]
print (type(my_list), my_list)
my_list[0] = 5
print (type(my_list), my_list)

 # Задание 3

my_tuple = (1, 2, 3, 4, 5)
print (type(my_tuple), my_tuple)
my_tuple[0] = 5
print (type(my_tuple), my_tuple)

# Задание 4

my_set = {1, 2, 3, 4, 5}
print (type(my_set), my_set)

# Задание 5

new_set = set(my_list)
print (type(new_set), new_set)

# Задание 6

my_dict = {"июнь": 30, "июль": 31, "август": 31}
print (type(my_dict), my_dict)

# Задание 7

my_range = range(10)
print (type(my_range), list(my_range))

 # Задание 8

a = 15
b = int("25")
sum_result = (a+b)
print("sum_result", sum_result, type(sum_result))

a = 15
b = "25"
sum_result = a + int(b)
print("sum_result", sum_result, type(sum_result))

password_letters = "mypassword"
password_digits = 1234
password = password_letters + str(password_digits)
print(type(password), password)
