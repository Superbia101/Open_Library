def pyramid_num() -> None:
    """Выводит на экран заполненную нечётными числами пирамиду.

    :return: None
    """

    num = int(input('Введите высоту пирамиды: '))
    print()
    temp: int = 1

    for row in range(1, num + 1):
        for col in range(1, 2 * num):
            if num + 2 * row > row + col > num and row % 2 == col % 2:
                print(temp, end=' ')
                temp += 2
            else:
                print(end='   ')

        print()


if __name__ == '__main__':
    pyramid_num()
