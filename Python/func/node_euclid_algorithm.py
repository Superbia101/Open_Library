#from math import gcd


def node_euclid_algorithm(num_1: int, num_2: int) -> int:
    """Поиск наибольшего общего делителя, через алгоритм Евклида.

    :param num_1: arg1
    :type num_1: int
    :param num_2: arg2
    :type num_2: int

    :rtype: int
    :return: num_2
    """
    
    num_1, num_2 = max(num_1, num_2), min(num_1, num_2)
    temp: int = num_1 % num_2
    while temp != 0:
        num_1, num_2 = num_2, temp
        temp = num_1 % num_2

    return num_2


num1 = int(input('Введите 1-е число: '))
num2 = int(input('Введите 2-е число: '))
print('НОД двух чисел:', node_euclid_algorithm(num1, num2))
#print('НОД двух чисел:', gcd(num1, num2)) # Проверка результата
