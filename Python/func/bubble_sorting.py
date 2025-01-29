from typing import List


def bubble_sorting(list_x: List[int], key: bool = True) -> List[int]:
    """Сортировка методом пузырька в порядке возрастания/убывания.

    :param list_x: Исходный список
    :type list_x: List[int]
    :param key: Параметр определяющий направление сортировки
    :type key: bool

    :rtype: List[int]
    :return: Отсортированный список
    """

    n: int = len(list_x)

    for _ in range(n):
        flag: bool = True

        for i in range(1, n):
            if key:
                if list_x[i - 1] > list_x[i]:
                    list_x[i], list_x[i - 1] = list_x[i - 1], list_x[i]
                    flag = False
            else:
                if list_x[i - 1] < list_x[i]:
                    list_x[i], list_x[i - 1] = list_x[i - 1], list_x[i]
                    flag = False
        if flag:
            break

    return list_x


if __name__ == "__main__":
    list_num: list[int] = [5, 2, 8, 1, 0, 4, 5, 7, 2, 3, 9, 6, 0]
    print(bubble_sorting(list_num))
