#Для решения данной задачи необходимо вычислить площади круга (π * r^2) и квадрата (a^2) и сравнить их.

import math

def larger_area(a, r):
    circle_area = math.pi * r**2
    square_area = a**2
    
    if circle_area > square_area:
        return "Круг", circle_area
    else:
        return "Квадрат", square_area

# Пример использования
a = 4
r = 3

shape, area = larger_area(a, r)
print(f"Фигура с большей площадью: {shape} (площадь = {area})")