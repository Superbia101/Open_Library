def retiring_list(men_num: int, rem_num: int) -> int:
    """На основе первого аргумента создаёт список элементов,
    производит удаление элементов списка правилом очерёдности
    на основе второго аргумента, передаёт последнее значение.

    :param men_num: arg1
    :type men_num: int
    :param rem_num: arg2
    :type rem_num: int

    :rtype: int
    :return: Последний элемент последовательности
    """
    men_list: list[int] = [num for num in range(1, men_num + 1)]
    num_start: int = 1
    
    while len(men_list) > 1:
        print('Текущий круг людей:', men_list)
        print('Начало счёта с номера', num_start)
        num_finish = men_list[(men_list.index(num_start) + rem_num - 1) % len(men_list)]
        num_start = men_list[(men_list.index(num_finish) + 1) % len(men_list)]
        print('Выбывает человек под номером', num_finish, end='\n\n')
        men_list.remove(num_finish)

    return men_list[0]


n_num = int(input('Кол-во человек: '))
k_num = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {k_num}-й человек', end='\n\n')
print('Остался человек под номером', retiring_list(n_num, k_num))
