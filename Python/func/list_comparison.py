from typing import List


def list_comparison(list_1: List[int], list_2: List[int]) -> bool:
    """Сравниваются (на предмет равенства) два числовых списка.

    :param list_1: Первый список
    :type list_1: List[int]
    :param list_2: Второй список
    :type list_2: List[int]

    :rtype: bool
    :return: True | False
    """

    x: int = 0
    flag: bool = False

    if len(list_1) == len(list_2) and hash(tuple(list_1)) == hash(tuple(list_2)):  # Сравнивается длина и хэш
        for i in range(len(list_1)):  # Проверка элементов, на случай коллизии хэша
            x += 1 if (list_1[i] == list_2[i]) else 0  # Подсчёт одинаковых элементов
        if x == len(list_1):  # Проверка кол-ва равных элементов
            flag = True

    return flag


if __name__ == '__main__':
    a = [1, 2, 0, 6]
    b = [1, 2, 0, 6, 8]
    print(list_comparison(a, b))
