# *** функции ввода-вывода, типы данных, арифметические операции ***

# функция ввода
# in_1 = input("введите первое целое число: ")
# in_2 = input("введите второе целое число: ")

# функция вывода
# print(in_1, in_2)
# print(in_1)
# print(in_2)
# конкатинация строк - старый способ фоматирования строк
# result = in_1 + in_2

# конвертация строковое число в целое число
# result = int(in_1) + int(in_2)
# print(result)

# способ форматирования строк " f - строка"
# fs = f"Первое число: {in_1}, Второе число: {in_2}"
# fs_2 = f"""
# Первое число: {in_1} 
# Второе число: {in_2}"""
# fs_3 = f"\nПервое число:\t {in_1} \nВторое число:\t {in_2}"
# print (fs)
# print (fs_2)
# print (fs_3)


# Типы данных 

# целочисленные типы данных
from xmlrpc.client import boolean


int_var = 275

# тип данных "числа с плавающей точкой" (пишутся через точку) - вещественные числа
float_var = 3.14

# строковые типы данных
char_var = 'A'
str_var = "hello, world"

# булевы типы данных Джордж Буль, булева алгебра, логика
boolean_var_t = True # 1
boolean_var_f = False # 0


# Арифметические операции

x = 9
y = 4
# сложение
res = x + y 

res = x - y

# умножение

res = x * y

# деление обычное (всегда возвращает число с плавающей точкой)
res_1= x / y
# целочисленное деление  (всегда возращают целую часть)
res_2 = x // y

# деление по остатку
res = x % y

# возведение в степень

res = x ** y

# корень числа 
# res = 100 ** (1/2)
import math
rest = math.sqrt (100)


# print (res_1)
# print(res_2)
print(res)