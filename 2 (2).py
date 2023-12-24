# Для решения данной задачи можно использовать формулу для вычисления расстояния между двумя точками в декартовой системе координат. 
# Необходимо вычислить расстояние от каждой точки до начала координат и выбрать точку с наименьшим расстоянием.


import math

def closer_to_origin(x1, y1, x2, y2):
    distance1 = math.sqrt(x1**2 + y1**2)
    distance2 = math.sqrt(x2**2 + y2**2)
    
    if distance1 < distance2:
        return x1, y1
    else:
        return x2, y2

# Пример использования
x1 = 3
y1 = 4
x2 = 1
y2 = 1
 
result_x, result_y = closer_to_origin(x1, y1, x2, y2)
print(f"Ближайшая точка к началу координат: ({result_x}, {result_y})")