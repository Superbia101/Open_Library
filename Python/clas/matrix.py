from __future__ import annotations


class Matrix:
    """Класс 'матрицы', имеет атрибуты: кол-во строк, кол-во столбцов, матрицу значений. Методы: конструктор, сложение,
    вычитание, умножение и транспонирование.
    """

    lines: int
    columns: int
    data: list[list[int]]

    def __init__(self, lines: int, columns: int) -> None:
        """Конструктор, создаёт поля.

        :param lines: Количество строк
        :type lines: int
        :param columns: Количество столбцов
        :type columns: int
        """

        self.lines = lines
        self.columns = columns
        self.data: list[list[int]] = [[0 for _ in range(columns)] for _ in range(lines)]

    def __str__(self) -> str:
        """Строковое представление объекта - отображение значений матрицы.

        :rtype: str
        :return: Значение поля data в строковом представлении
        """

        string: str = ''
        for lists in self.data:
            for nums in lists:
                string += '{}\t'.format(nums)
            string += '\n'
        return string

    def add(self, other: Matrix) -> list[list[int]]:
        """Суммирование матриц, возвращает результат суммы из вызываемой и переданной матрицы.

        :param other: Переданная матрица
        :type other: Объект класса Matrix

        :except ValueError: Разная размерность слагаемых
        :except Exception: Остальное

        :rtype: list[list[int]]
        :return: Матрица результат
        """

        try:
            assert self.lines == other.lines and self.columns == other.columns, 'ValueError: Неверный размер элементов!'
        except ValueError as err:
            print('Операция отменена, причина: разная размерность матриц! {}'.format(err))
        else:
            try:
                return [[self.data[lin][col] + other.data[lin][col] for col in range(self.columns)]
                        for lin in range(self.lines)]
            except Exception as err:
                print('Операция отменена, причина: {}'.format(err))

    def subtract(self, other: Matrix) -> list[list[int]]:
        """Разность матриц, возвращает результат разности из вызываемой и переданной матрицы.

        :param other: Переданная матрица
        :type other: Объект класса Matrix

        :except ValueError: Разная размерность слагаемых
        :except Exception: Остальное

        :rtype: list[list[int]]
        :return: Матрица результат
        """

        try:
            assert self.lines == other.lines and self.columns == other.columns, 'ValueError: Неверный размер элементов!'
        except ValueError as err:
            print('Операция отменена, причина: разная размерность матриц! {}'.format(err))
        else:
            try:
                return [[self.data[lin][col] - other.data[lin][col] for col in range(self.columns)]
                        for lin in range(self.lines)]
            except Exception as err:
                print('Операция отменена, причина: {}'.format(err))

    def multiply(self, other: Matrix) -> list[list[int]]:
        """Произведение матриц, возвращает результат произведения из вызываемой и переданной матрицы.

        :param other: Переданная матрица
        :type other: Объект класса Matrix

        :except ValueError: Неподходящая размерность слагаемых
        :except Exception: Остальное

        :rtype: list[list[int]]
        :return: Матрица результат
        """

        try:
            assert self.columns == other.lines, 'ValueError: Неверный размер элементов!'
        except ValueError as err:
            print('Операция отменена, причина: разная размерность матриц! {}'.format(err))
        else:
            try:
                return [[sum(i * j for i, j in zip(lin, col)) for col in zip(*other.data)] for lin in self.data]
            except Exception as err:
                print('Операция отменена, причина: {}'.format(err))

    def transpose(self) -> list[list[int]]:
        """Транспонирования матрицы.

        :rtype: list[list[int]]
        :return: Матрица результат транспонирования исходной
        """

        return [list(row) for row in zip(*self.data)]


# Примеры работы с классом:

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())
