# ** Дополнительно **
# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где

# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# Требуется найти N-е число Фибоначчи

def Fib(n):
    if n in [1,2]:
        return 1
    return Fib(n-1) + Fib(n-2)

n = int(input('Enter N: '))

# print(Fib(n))

list = [0,1]

for i in range(1,n):
    list.append(Fib(i))
# print(list)
print(max(list))




