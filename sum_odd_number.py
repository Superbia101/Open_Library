def sum_nech(num: str):
    """функция сумирует неч числа до N"""
    return sum([i for i in range(int(num) + 1) if i % 2 != 0])




print(sum_nech(input('Введите число: ')))
