def snake(line: int, column: int) -> None:
    """Создаёт и выводит матрицу, заполненную числами по спирали.

    :param line: Кол-во строк
    :type line: int
    :param column: Кол-во столбцов
    :type column: int

    :return: None
    """

    list_num = [[0] * column for _ in range(line)]

    num, temp, i, j = 0, 0, 0, 0

    while num < line * column: 
        for j in range(temp, column - temp):  # Заполнение верхнего октанта
            if list_num[i][j] == 0:
                num += 1
                list_num[i][j] = num

        for i in range(temp, line - temp):  # Заполн. левого октанта
            if list_num[i][j] == 0:
                num += 1
                list_num[i][j] = num

        for j in range(column - 1 - temp, temp - 1, -1):  # Заполн. нижнего окт.
            if list_num[i][j] == 0:
                num += 1
                list_num[i][j] = num

        for i in range(line - 1 - temp, temp, -1):  # Заполн. правого окт.
            if list_num[i][j] == 0:
                num += 1
                list_num[i][j] = num

        temp += 1  # Переход на след. круг

    print('Матрица - "змейка"!')

    for row in list_num:
        print('\t'.join([str(elem) for elem in row]))


if __name__ == '__main__':
    n, m = int(input('Введите кол-во строк: ')), int(input('Введите кол-во столбцов: '))
    print()
    snake(n, m)
