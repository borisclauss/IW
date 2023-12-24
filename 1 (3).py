# Дано натуральное n. Вычислить: 1/sin1 + 1/sin1+sin2 + ... + 1/sin1+...sinn

import math
def sin_sum(n):
    sin_sum = 0
    current_sum = 0
    for i in range(1, n+1):
        current_sum += i
        sin_sum += 1 / math.sin(current_sum)
    return sin_sum

print(sin_sum(5))