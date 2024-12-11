def auxiliary_division_list(works_list: list[int]) \
        -> tuple[list[int], list[int], list[int]]:
    """Принимает на вход список, а возвращает три списка с элементами меньше,
    равными и больше опорного. Опорный элемент - крайний правый.

    :param works_list: arg1 Исходный список
    :type works_list: list[int]

    :rtype: tuple[list[int], list[int], list[int]]
    :return: Три списка: элементы меньше опорного, равные опорному и больше опорного
    """

    less_list, more_list, equal_list = [], [], []

    for _, elem in enumerate(works_list):
        if elem < works_list[-1]:
            less_list.append(elem)
        elif elem > works_list[-1]:
            more_list.append(elem)
        else:
            equal_list.append(elem)

    return less_list, equal_list, more_list


def quicksort_hoare(works_list: list[int]) -> list[int]:
    """Алгоритм быстрой сортировки (сортировка Хоара), опорный элемент крайний правы.

    :param works_list: arg1 Список для сортировки
    :type works_list: list[int]

    :rtype: list[int]
    :return: Отсортированный список
    """

    works_tuple: tuple[list[int], list[int], list[int]] = auxiliary_division_list(works_list)

    temp: dict[int: list] = {}

    for index in [0, 2]:
        for num in works_tuple[index][:-1]:
            if num != works_tuple[index][-1]:
                temp[index] = quicksort_hoare(works_tuple[index])
                break
        else:
            temp[index] = works_tuple[index]

    return temp[0] + works_tuple[1] + temp[2]


# num_list = [5, 8, 9, 4, 2, 9, 1, 8]
num_list = [1, 105, 8, 9, 4, 10, 11, 34, 99, 2, 2, 9, 1, 8]
print('Исходный список:', num_list)
print('Отсортированный список:', quicksort_hoare(num_list))
