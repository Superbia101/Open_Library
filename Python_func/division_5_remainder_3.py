"""Список из чисел, которые при делении на 5 дают в остатке 3
два варианта программы: first и second."""
"""first = [i for i in range(int(input("Ведите предел: "))) if i % 5 == 3]
print(first)
second = [5 * i + 3 for i in range(int(input("Ведите предел: ")))]
print(second)"""

""" можно усложнить"""
#div - делитель, введённый с клавиатуры
#rem - остаток, введённый с клавиатуры
"""div = int(input("При делении на что (больше нуля)? "))
rem = int(input("Остаток (должен быть меньше делителя): "))
third = [i for i in range(int(input("Ведите предел: "))) if i % div == rem]
print(third)"""


def division(div: int = 2, rem: int = 1, num: int = 10) -> list[int]:
    """Выводит список из нечётных чисел, с параметрами - числа имеют
    определённый остаток от определённого делителя.

    :param div: arg1 делитель
    :type div: int
    :param rem: arg2 остаток
    :type rem: int
    :param num: arg3 кол-во
    :type num: num

    :raises ValueError: if arg2 >= to arg1

    :rtype: list[int]
    :return: list_num
    """
    list_num: list[int] = []
    if rem >= div:
        raise ValueError("Таких чисел не существует!")
    else:
        temp: int = 0  # Число для проверки
        while len(list_num) < num:
            temp += 1  # Возрастание
            if temp % div == rem:  # Проверка на условия
                list_num.append(temp)
        return list_num


try:
    num_1 = int(input("При делении на что (больше нуля)? "))
    num_2 = int(input("Остаток (должен быть меньше делителя): "))
    num_3 = int(input("Введите кол-во: "))
    print(division(num_1, num_2, num_3))
except:
    print("Должно быть число!")
