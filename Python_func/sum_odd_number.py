def sum_odd(num: str) -> int:
    """Функция суммирует нечётные числа до аргумента.

    :param num: arg1
    :type num: str

    :rtype: int
    :return: sum( i % 2 != 0 .. N)
    """
    return sum([i for i in range(int(num) + 1) if i % 2 != 0])


print(sum_odd(input('Введите число: ')))
