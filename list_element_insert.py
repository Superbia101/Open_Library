from random import seed, randint


def element_insert(num: int):
    """Между каждой парой элем. списка заданной длины вставляется новый, равный сумме соседних.

    :param num: arg1
    :type num: int

    :return: Вывод на экран списка
    """
    seed(2024)
    list_1: list[int] = [randint(0, 9) for _ in range(num)]  # Создаём случ. список
    print('Случайный список:', list_1)
    list_2: list[int] = list_1[:]  # Поверхностная копия
    temp: int = 1  # Поправка на сдвиг
    for i in range(len(list_1) - 1):
        list_2[i + temp:i + temp] = [list_1[i] + list_1[i + 1]]
        temp += 1
    print('Результат:', list_2)


element_insert(10)
