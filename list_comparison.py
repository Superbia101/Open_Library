def list_comparison(list_1: list[int], list_2: list[int]):
    """Сравниваются (на предмет равенства) два числовых списка.

    :param list_1: arg1
    :type list_1: list[int]
    :param list_2: arg2
    :type list_2: list[int]
    :return: Выводит на экран сообщение
    """
    x: int = 0
    if len(list_1) == len(list_2):  # Сравнивается длина
        for i in range(len(list_1)):
            x += 1 if (list_1[i] == list_2[i]) else 0  # Подсчёт одинаковых элементов
        if x == len(list_1):  # Проверка кол-ва элементов
            print("Равны!")
        else:
            print("Не равны!")
    else:
        print("Не равны!")


a = [1, 2, 0, 6]
b = [1, 2, 0, 6]
list_comparison(a, b)
