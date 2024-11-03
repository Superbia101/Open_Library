def output_content_number(num: int) -> None:
    """Определяет сколько в целом числе различных цифр и выводит на экран.

    :param num: arg1
    :type num: int

    :return: Выводит результат на экран
    """
    count: dict[int, int] = dict()

    while num != 0:
        count[num % 10] = count.get(num % 10, 0) + 1
        num //= 10

    for key, val in sorted(count.items()):
        print(key, " - ", val)


n = int(input('Введите целое число большой разрядности: '))
output_content_number(n)
