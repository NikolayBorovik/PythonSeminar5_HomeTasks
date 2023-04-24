# Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) 
# для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def Factorial(n):
    if n == 1:
        return n
    else:
        return n*Factorial(n-1)
 
def Triangle(n):
    if n == 1:
        return n
    else:
        return n+Factorial(n-1)

n = int(input('Enter N: '))

print(Factorial(n))
print(Triangle(n))