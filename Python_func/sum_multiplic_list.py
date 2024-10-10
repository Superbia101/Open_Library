def sum_multiplic_list(list_1: list[int], list_2: list[int]) -> int:
    """Сумма попарных произведений элементов списков. Если один меньше, он прокручивается.

    :param list_1: arg1
    :type list_1: list[int]
    :param list_2: arg2
    :type list_2: list[int]

    :rtype: int
    :return: sum(l1[i] * l2[i] for i in len)
    """
    if len(list_1) != len(list_2):
        if len(list_1) < len(list_2):
            list_1, list_2 = list_2, list_1
        item: int = 0
        while len(list_1) != len(list_2):
            list_2.append(list_2[item])
            item += 1
    return sum([symbol * list_2[index] for index, symbol in enumerate(list_1)])


#A = [1, 2, 3, 4, 5, 6]
#B = [0, 7, 8]
A = [1, 0, 1]
B = [i for i in range(30)]
print(sum_multiplic_list(A, B))
