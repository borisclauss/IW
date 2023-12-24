#Дано действительное число x, натуральное число n. Вычислить: x^1/1! + x^2/2! + x^3/3! + ... + x^n/n!

def compute_sum(x, n):
   sum = 0
   factorial = 1
   
   for i in range(1, n+1):
      factorial *= i
      sum += x ** i / factorial
   
   return sum

x = float(input("Введите значение x: "))
n = int(input("Введите значение n: "))

result = compute_sum(x, n)
print("Сумма последовательности:", result)