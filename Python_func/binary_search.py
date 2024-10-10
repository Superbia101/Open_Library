def binary_search(low_limit: int, big_limit: int):
    """Поиск числа в отрезке через алгоритм бинарного поиска.

    :param low_limit: arg1
    :type low_limit: int
    :param big_limit: arg2
    :type big_limit: int
    :return: Ничего не возвращает
    """
    while True:
        middle: int = (low_limit + big_limit) // 2
        print('Твое число равно, меньше или больше, чем число', str(middle) + '?')
        num = int(input())
        if num == 1:
            break
        elif num == 2:
            low_limit = middle
        else:
            big_limit = middle
    print('Число равно:', middle, '!')


print('Загадайте число от 1 до 100')
print('Отвечайте на запросы компьютера: 1 - равно, 2 - больше, 3 - меньше')
print('Начали!', end='\n\n')
binary_search(0, 100)
