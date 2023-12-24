# Для решения данной задачи можно вычислить расстояние от точки до центра круга и сравнить его с радиусом круга.

import math

def point_in_circle(x, y, x0, y0, r):
    distance = math.sqrt((x - x0)**2 + (y - y0)**2)
    
    if distance <= r:
        return True
    else:
        return False

# Пример использования
x = 2
y = 3
x0 = 1
y0 = 1
r = 2

if point_in_circle(x, y, x0, y0, r):
    print("Точка попадает в круг")
else:
    print("Точка не попадает в круг")