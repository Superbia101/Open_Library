def sum_odd(num: str) -> int:
    """Функция суммирует нечётные числа до аргумента.

    :param num: Верхний придел
    :type num: str

    :rtype: int
    :return: Сумма
    """

    return sum([i for i in range(int(num) + 1) if i % 2 != 0])


if __name__ == "__main__":
    print(sum_odd(input('Введите число: ')))
