def second_max(list_num: list[int | float], first: bool = False) -> list[int | float]:
    """Функция возвращает первый/второй максимум и его индекс из переданного списка.

    :param list_num: Список значений
    :type list_num: list[int | float]
    :param first: Флаг работы функции
    :type first: bool

    :rtype: list[int | float]
    :return: list(max, index(max))
    """

    if first:  # Если функции передан второй аргумент - возвращает второй макс
        list_num.remove(max(list_num))

    return [max(list_num), list_num.index(max(list_num))]


def second_max_modified(list_num: list | tuple) -> list[tuple]:
    """Функция возвращает первый и второй максимум и, их индексы из списка.

    :param list_num: Список значений
    :type list_num: list | tuple

    :rtype: list[tuple]
    :return: Максимумы списка: 1-й, его индекс и 2-рой, и его индекс
    """

    first, second = list_num[:2]  # Берём первое и второе значение из списка
    f_index, s_index = 0, 1  # Значения индексов

    if first < second:  # Распределяем их
        first, second = second, first
        f_index, s_index = 1, 0

    for i in range(2, len(list_num)):  # Сравниваем все значения с 1-вым макс
        if first < list_num[i]:
            first, second = list_num[i], first  # Заменяем на большие
            f_index, s_index = i, f_index  # Их индексы тоже
        elif second < list_num[i]:  # Сравниваем 2-той
            second = list_num[i]
            s_index = i

    return [(first, f_index), (second, s_index)]


if __name__ == "__main__":
    a: list[int] = [1, 2, 3, 4, 5, 23, 6, 7, 3, 89, 4]
    #print(*second_max(a,1))
    print(second_max_modified(a))
