def output_nums(num: int) -> None:
    """Выводит на экран все числа от 1 до переданного.

    :param num: arg
    :type num: int

    :return: Выводит на экран
    """
    if num != 1:
        output_nums(num - 1)

    print(num, end='\n\n')


output_nums(int(input('Введите num: ')))
