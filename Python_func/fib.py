"""Число из последовательности Фибоначчи."""
num = int(input("Ведите число: "))
a, b = 1, 1

for i in range(2, num):
    a, b = a + b, a

print(a)
