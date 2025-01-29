from math import gcd


# наивный алгоритм (линейное время работы)
def gcd1(a: int, b: int) -> int:

    assert a >= 0 and b >= 0

    for d in reversed(range(max(a, b) + 1)):
        if d == 0 or a % d == b % d == 0:
            return d


def node_euclid_algorithm(num_1: int, num_2: int) -> int:
    """Поиск наибольшего общего делителя, через алгоритм Евклида.

    :param num_1: Первое число
    :type num_1: int
    :param num_2: Второе число
    :type num_2: int

    :assert: a >= 0 and b >= 0

    :rtype: int
    :return: НОД
    """

    assert num_1 >= 0 and num_2 >= 0

    num_1, num_2 = sorted([num_1, num_2])

    while num_1:
        num_1, num_2 = num_2 % num_1, num_1

    return num_2


if __name__ == "__main__":
    num1 = int(input("Введите 1-е число: "))
    num2 = int(input("Введите 2-е число: "))
    print("НОД двух чисел:", node_euclid_algorithm(num1, num2))
    print("НОД двух чисел:", gcd(num1, num2))  # Проверка результата
