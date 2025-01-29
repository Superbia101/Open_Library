def output_content_number(num: int) -> None:
    """Определяет сколько в целом числе различных цифр и выводит на экран.

    :param num: Число
    :type num: int

    :return: None
    """

    count: dict[int, int] = dict()

    while num != 0:
        count[num % 10] = count.get(num % 10, 0) + 1
        num //= 10

    for key, val in sorted(count.items()):
        print(key, " - ", val)


if __name__ == "__main__":
    n = int(input("Введите целое число большой разрядности: "))
    output_content_number(n)
