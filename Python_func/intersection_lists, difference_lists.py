def intersection_lists(*lists: list[int]) -> list[int]:
    """Возвращает список из элементов которые присутствуют во всех переданных списках.

    :param lists: *arg
    :type: list[int]

    :rtype: list[int]
    :return: all_num_list
    """
    all_num_list: list[int] = []

    for num in lists[0]:
        for index in range(1, len(lists)):
            if num not in lists[index]:
                break
        else:
            all_num_list.append(num)

    return all_num_list


def difference_lists(*lists: list[int]) -> list[int]:
    """Возвращает список из элементов первого списка, которых нет во всех переданных остальных списках.

    :param lists: *arg
    :type: list[int]

    :rtype: list[int]
    :return: all_num_list
    """
    all_num_list: list[int] = []

    for num in lists[0]:
        for index in range(1, len(lists)):
            if num in lists[index]:
                break
        else:
            all_num_list.append(num)

    return all_num_list


array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

print('Задача 1:')
print('Решение без множеств:', *intersection_lists(array_1, array_2, array_3))
print('Решение с множествами:', *(set(array_1) & set(array_2) & set(array_3)))
print('\n\nЗадача 2:')
print('Решение без множеств:', *difference_lists(array_1, array_2, array_3))
print('Решение с множествами:', *(set(array_1) - set(array_2) - set(array_3)))
