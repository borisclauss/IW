#По данным сторонам прямоугольника вычислить его периметр, площадь и длину диагонали.

import math

# Вводим стороны прямоугольника
a = float(input("Введите значение стороны a: "))
b = float(input("Введите значение стороны b: "))

# Вычисляем периметр прямоугольника (в единицах длины)
perimeter = 2 * (a + b)

# Вычисляем площадь прямоугольника (в квадратных единицах)
area = a * b

# Вычисляем длину диагонали прямоугольника (в единицах длины)
diagonal_length = math.sqrt(a**2 + b**2)

# Выводим результаты
print("Периметр прямоугольника:", perimeter)
print("Площадь прямоугольника:", area)
print("Длина диагонали прямоугольника:", diagonal_length)