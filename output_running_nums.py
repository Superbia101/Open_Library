def output_running_nums(symbol_list: list, num: int) -> list:
    """Сдвигает элементы списка вправо на заданное кол-во позиций.

    :param symbol_list: arg1
    :type symbol_list: list
    :param num: arg2
    :type num: int

    :raises ValueError: if abs(num) > elements symbol_list

    :rtype: list
    :return: new_symbol_list
    """
    if abs(num) > len(symbol_list):
        raise ValueError('Ошибка! Недопустимый размер.')
    new_symbol_list: list[int] = [0] * len(symbol_list)

    for index, _ in enumerate(symbol_list):
        new_symbol_list[index] = symbol_list[index - num]

    return new_symbol_list


old_list: list[int] = []

for elem in range(int(input('Количество элементов: '))):
    old_list.append(int(input(f'Введите {elem + 1} элемент: ')))

k_num: int = int(input('Сдвиг: '))
print('Изначальный список:', old_list)
print('Сдвинутый список:', output_running_nums(old_list, k_num))
