def sum_multiplic_list(list_1: list[int], list_2: list[int]) -> int:
    """Сумма попарных произведений элементов списков. Если один из них меньше, он прокручивается с начала.

    :param list_1: Первый список
    :type list_1: list[int]
    :param list_2: Второй список
    :type list_2: list[int]

    :rtype: int
    :return: Сумма попарных произведений
    """

    if len(list_1) != len(list_2):
        if len(list_1) < len(list_2):
            list_1, list_2 = list_2, list_1

        item: int = 0
        while len(list_1) != len(list_2):
            list_2.append(list_2[item])
            item += 1

    return sum([symbol * list_2[index] for index, symbol in enumerate(list_1)])


if __name__ == "__main__":
    # A = [1, 2, 3, 4, 5, 6]
    # B = [0, 7, 8]
    A = [1, 0, 1]
    B = [i for i in range(30)]
    print(sum_multiplic_list(A, B))
