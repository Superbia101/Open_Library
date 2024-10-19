import math


def count_exponent_degree(quant: float) -> list[float | int]:
    """Определяет значение степени экспоненциального представления числа.

    :param quant: arg1
    :type quant: float

    :rtype: list[float | int]
    :return: Список из целой части и степени
    """
    count: int = 0
    if abs(quant) >= 10:
        while abs(quant) >= 10:
            quant /= 10
            count += 10
    elif abs(quant) < 1:
        while abs(quant) < 1:
            quant *= 10
            count -= 1
    return [quant, count]
    #print(f'{quant}e{count}')


def count_exponent_degree_2(quant: float) -> list[float | int]:
    """Определяет значение степени экспоненциального представления числа.

    :param quant: arg1
    :type quant: float

    :rtype: list[float | int]
    :return: Список из целой части и степени
    """
    flag: bool = quant < 0
    quant = abs(quant)
    count: int = math.floor(math.log10(quant))
    quant = quant / 10 ** count
    quant = quant * (-1) if flag else quant
    return [quant, count]
    #print(f'{quant}e{count}')


def check_exponent_degree(tax: float, new_tax: float) -> None:
    """Проверка порядка экспоненциального представления после суммы.

    :param tax: arg1
    :type tax: float
    :param new_tax: arg2
    :type new_tax: float

    :return: Выводит на экран
    """
    new_tax += tax
    tax = count_exponent_degree(tax)
    new_tax = count_exponent_degree(new_tax)
    if new_tax[1] > tax[1]:
        print('Степень экспоненты суммы увеличилась')
    elif new_tax[1] < tax[1]:
        print('Степень экспоненты суммы уменьшилась')
    else:
        print('Степень экспоненты не изменилась')


num = float(input('Введите бюджет страны: '))
#new_num = float(input('Новые поступления (налог): '))
#check_exponent_degree(num, new_num)
print(count_exponent_degree_2(num))
