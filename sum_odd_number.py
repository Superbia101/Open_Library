def sum_nech(N):
    "Функция сумирует неч числа до N"
    a=[i for i in range(int(N) + 1) if i % 2 != 0]
    return sum(a)
n=input()
print(sum_nech(n))
