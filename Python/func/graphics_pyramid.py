def pyramid() -> None:
    """Выводит на экран пирамидку, заполненную символами хештега(#).

    :return: None
    """

    num = int(input('Введите высоту пирамиды: '))

    for row in range(num + 1):
        for col in range(2 * num + 1):
            if num + 2 * row > row + col > num:
                print('#', end='')
            else:
                print(' ', end='')

        print()


if __name__ == '__main__':
    pyramid()
