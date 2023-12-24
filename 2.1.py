# Дано действительное число x, натуральное число n. Вычислить: x(x-n)(x-2n)(x-3n)...(x-n^2)

def multiply_expression(x, n):
    result = 1
    
    for i in range(1, n+1):
        result *= (x - i*n)
    
    return result

x = float(input("Введите действительное число x: "))
n = int(input("Введите натуральное число n: "))

print("Результат:", multiply_expression(x, n))