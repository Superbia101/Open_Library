def output_nums(num: int) -> None:
    """Выводит на экран все числа от 1 до переданного. Рекурсивно.

    :param num: Переданное значение
    :type num: int

    :return: None
    """

    if num != 1:
        output_nums(num - 1)

    print(num, end="\n\n")


if __name__ == "__main__":
    output_nums(int(input("Введите num: ")))
