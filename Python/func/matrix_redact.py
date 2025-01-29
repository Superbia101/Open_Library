from random import seed, randint


def matrix_redact(line: int, column: int, re_line: int, re_column: int) -> None:
    """Создаёт и выводит вложенный список n на m, у которого удаляется заданные строка и столбец.

    :param line: Кол-во строк
    :type line: int
    :param column: Кол-во столбцов
    :type column: int
    :param re_line: Удаляемая строка
    :type re_line: int
    :param re_column: Удаляемый столбец
    :type: re_column: int

    :return: None
    """

    seed(2024)

    rand_list: list[list[int]] = [[randint(0, 9) for _ in range(column)] for _ in range(line)]

    # Создаётся матрица случайных значений.
    for row in rand_list:  # Демонстрация результата
        print(' '.join([str(elem) for elem in row]))

    print()
    rand_list.pop(re_line)  # Удаляем строку

    for i in range(len(rand_list)):  # Удаляем столбец
        rand_list[i].pop(re_column)

    for row in rand_list:  # Демонстрация результата
        print(' '.join([str(elem) for elem in row]))


if __name__ == '__main__':
    matrix_redact(5, 7, 3, 3)
