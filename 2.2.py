# Дано действительное число x, натуральное число n. Вычислить: 1/x + 1/x(x+1) + ... + 1/x(x+1)...(x+n)

def calculate_sum(x, n):
    result = 0
    denominator = 1
    i = 0
    while i <= n:
        denominator *= x + i
        result += 1 / (x * denominator)
        i += 1
    return result

x = float(input("Введите действительное число x: "))
n = int(input("Введите натуральное число n: "))

print("Сумма ряда равна:", calculate_sum(x, n))