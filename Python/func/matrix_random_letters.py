from random import seed, randint


def my_list(line: int, column: int) -> None:
    """Создаёт и выводит вложенный список n на m, заполн. случ. буквами.

    :param line: arg1
    :type line: int
    :param column: arg2
    :type column: int

    :return: Выводит матрицу на экран
    """
    seed(2024)

    rand_list: list[list[int | str]] = [[0] * column for _ in range(line)]

    for i in range(line):
        for j in range(column):
            rand_list[i][j] = chr(randint(ord('A'), ord('Z')))
    for row in rand_list:
        print(' '.join(row))


n, m = 4, 4
my_list(n, m)
