from random import seed, randint


def sort_special(num: int):
    """Создаёт случ список и преобразовывает в перемежающуюся последовательность.

    :param num: arg1
    :type num: int

    :return: Выводит список на экран
    """
    seed(2024)
    rand_list: list[int] = [randint(0, 9) for _ in range(num)]  # Создаём случ. список
    print('Случайный список:', rand_list)
    even: list[int] = sorted(rand_list[0::2])
    uneven: list[int] = sorted(rand_list[1::2], reverse=True)
    print('Чётные эл. по возрастанию:', even)
    print('Нечётные по убыванию', uneven)
    fin_list: list[int] = []
    index: int = 0
    while len(fin_list) < len(rand_list):
        fin_list.append(even[index])
        fin_list.append(uneven[index])
        index += 1
    print('Итоговый список:', fin_list)


sort_special(20)
    
