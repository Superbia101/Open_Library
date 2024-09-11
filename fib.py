"""число из последовательности Фибоначчи"""

n = int(input("Ведите число: "))
a, b = 1, 1
for i in range(2, n):
    a, b = a + b, a
print(a)
