def merge_sorted_lists(list_1: list[int | float], list_2: [int | float]) \
        -> list[int | float]:
    """Объединяет два отсортированных списка чисел в один
    отсортированный без дубликатов.

    :param list_1: arg1
    :type list_1: list[int | float]
    :param list_2: arg2
    :type list_2: list[int | float]

    :rtype: list[int | float]
    :return: list_1
    """
    list_1.extend(list_2)
    list_1.sort()

    for symbol in list_1:
        temp: int = list_1.count(symbol)
        if temp > 1:
            for _ in range(temp - 1):
                list_1.remove(symbol)

    return list_1


# Пример использования:
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)
