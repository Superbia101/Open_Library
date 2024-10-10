def output_running_nums(symbol: list | str, num: int) -> list | str:
    """Сдвигает элементы списка/строки вправо на заданное кол-во позиций.

    :param symbol: arg1
    :type symbol: list | str
    :param num: arg2
    :type num: int

    :rtype: list | str
    :return: new_symbol
    """
    new_symbol: list = [0] * len(symbol)

    for index, _ in enumerate(symbol):
        new_symbol[index] = symbol[(index - num) % len(symbol)]

    return new_symbol if type(symbol) is list else ''.join(new_symbol)


# old_list: list[int | str] = []
#
# for elem in range(int(input('Количество элементов: '))):
#     old_list.append(int(input(f'Введите {elem + 1} элемент: ')))
#old_list = 'hello'
#k_num = int(input('Сдвиг: '))
#print('Изначальный список:', old_list)
#print('Сдвинутый список:', output_running_nums(old_list, k_num))


old_list: str = input('Первая строка: ')
new_list: str = input('Вторая строка: ')
if len(old_list) == len(new_list):
    if old_list == new_list:
        print('Они одинаковы, сдвиг не нужен.')
    else:
        for k_num in range(1, len(new_list) - 1):
            if old_list == output_running_nums(new_list, k_num):
                print(f'Первая строка получается из второй со сдвигом {k_num}.')
                break
        else:
            print('Первую строку нельзя получить из второй с помощью циклического сдвига.')


