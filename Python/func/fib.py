"""Число из последовательности Фибоначчи."""
"""num = int(input("Ведите число: "))
a, b = 1, 1

for _ in range(2, num):
    a, b = a + b, a

print(a)"""


"""Даны целые числа (1 <= n <= 10**18) и (2 <= m <= 10**5), необходимо
найти остаток от деления n-го числа Фибоначчи на m. Использовал период Пизано."""

def fib_mod(n: int, m: int) -> int:
    a: int = 1
    b: int = 1
    list_mod: list[int] = [0, 1]
    
    while True:
        a, b = a + b, a
        list_mod.append(b % m)
        
        if list_mod[-2:] == [0, 1]:
            break
    
    return list_mod[n % (len(list_mod) - 2)]


print(fib_mod(1598753, 25897))
