def comparison_real_numbers(
    number_sum_1: float, number_sum_2: float, number_raz: float, precision: float
) -> bool:
    """Сравнение суммы двух вещественных чисел с третьим с точностью: до 15-го знака.

    :param number_sum_1: arg1
    :type number_sum_1: float
    :param number_sum_2: arg2
    :type number_sum_2: float
    :param number_raz: arg3
    :type number_raz: float
    :param precision: arg4
    :type precision: float

    :rtype: bool
    :return: Если True - то сумма равна 3-ему аргументу с заданной точностью
    """

    return abs((number_sum_1 + number_sum_2) - number_raz) < precision


if __name__ == "__main__":
    num = 1.1
    num_2 = 2.2
    num_3 = 3.3
    num_4 = 1e-15
    print(comparison_real_numbers(num, num_2, num_3, num_4))
