<<<<<<< HEAD
def bubble_sorting(list_x: list[int]) -> list[int]:
    """Сортировка методом пузырька в порядке возрастания.

    :param list_x: arg1
    :type list_x: list[int]

    :rtype: list[int]
    :return: list_x
    """
    for _ in range((len(A) + 1) // 2):
        for i in range(1, len(A)):
            if list_x[i - 1] > list_x[i]:
                list_x[i], list_x[i - 1] = list_x[i - 1], list_x[i]         
    return list_x





list_num: list[int] = [5, 2, 8, 1, 0, 4, 5, 7, 2, 3, 9, 6, 0]
print(bubble_sorting(list_num))
