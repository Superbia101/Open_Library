from typing import Literal


class Cell:
    """
    Класс для представления клетки игровой доски.

    ...

    Скрытые Атрибуты
    ________________
    __num : int
        номер ячейки
    __in_cell : Literal['', 'X', 'O']
         хранимое значение (строго заданный список)

    Методы
    ------
    __init__(num: int) -> None
        создаёт атрибуты
    get_in_cell() -> Literal['', 'X', 'O']
        геттер содержимого клетки
    set_in_cell(in_cell: Literal['', 'X', 'O'] = '') -> None
        сеттер содержимого клетки
    """

    __num: int
    __in_cell: Literal['', 'X', 'O']

    def __init__(self, num: int) -> None:
        """Конструктор класса 'клетки', создаёт поля: номер клетки и содержимое.

        :param num: Номер клетки
        :type num: int
        """

        self.__num = num
        self.set_in_cell()

    def get_in_cell(self) -> Literal['', 'X', 'O']:
        """Геттер, содержимого клетки.

        :rtype: Literal['', 'X', 'O']
        :return: Содержимое клетки.
        """

        return self.__in_cell

    def set_in_cell(self, in_cell: Literal['', 'X', 'O'] = '') -> None:
        """Сеттер, содержимого клетки, по умолчанию путая строка.

        :param in_cell: Содержимое клетки игрового поля.
        :type in_cell: Literal['', 'X', 'O']

        :raise ValueError: Что-то за пределами допустимых значений ('', 'X', 'O').
        """

        if in_cell in ('', 'X', 'O'):
            self.__in_cell = in_cell
        else:
            raise ValueError('Неверное значение содержимого клетки!')


class Board:
    """
    Класс для представления игрового поля.

    ...

    Атрибуты
    ________
    state_board : list[list[Cell]]
        вложенный список с объектами класса Cell, представление игрового поля состоящего из клеток

    Скрытые Атрибуты
    ________________
    __n : int
        размер стороны игровой доски в игровых клетках

    Методы
    ------
    __init__(n: int = 3) -> None
        создаёт атрибуты
    get_n() -> int
        геттер размера стороны игровой доски
    set_n(n: int) -> None
        сеттер размера стороны игровой доски
    change_state_cell(num: int, symbol: Literal['', 'X', 'O']) -> bool
        метод заполнения ячеек
    check_final() -> bool
        метод проверки условия завершения партии
    """

    state_board: list[list[Cell]]
    __n: int

    def __init__(self, n: int = 3) -> None:
        """Создаёт список объектов-клеток игрового поля, размер поля определяется параметром 'n'(по умолчанию 3*3=9).

        :param n: Размер стороны игровой доски в игровых клетках, должно быть больше 1.
        :type n: int
        """

        self.set_n(n)
        # создаёт матрицу (список вложенных списков n элементов в n списках) объектов-ячеек с нумерацией от 1 по n ** 2
        self.state_board: list[list[Cell]] = [[Cell(obj) for obj in range(index, index + n)]
                                              for index in range(1, n ** 2, n)]

    def get_n(self) -> int:
        """Геттер, стороны игровой доски в игровых клетках.

        :rtype: int
        :return: Количество клеток в стороне игрового поля.
        """

        return self.__n

    def set_n(self, n: int) -> None:
        """Сеттер, стороны игровой доски в игровых клетках.

        :param n: Количество клеток в стороне игрового поля.
        :type n: int

        :raise ValueError: При значении n < 1 и/или не тип int.
        """

        if n > 1 and n % 1 == 0:
            self.__n = n
        else:
            raise ValueError('Неверное значение размера игрового поля!')

    def change_state_cell(self, num: int, symbol: Literal['', 'X', 'O']) -> bool:
        """Метод получает номер клетки и, если клетка не занята, меняет её состояние.

        :param num: Номер клетки состояние которой пробуют поменять.
        :type num: int
        :param symbol: Новое значение клетки.
        :type symbol: Literal['', 'X', 'O']

        :raise ValueError: При 'num' выходящем за пределы значения ячеек.

        :rtype: bool
        :return: Если состояние удалось изменить, метод возвращает True, иначе возвращается False.
        """

        assert num in (range(1, self.__n ** 2 + 1)), (
            'ValueError: Номер клетки за пределами допустимых значений от 1 до {}!'.format(self.__n ** 2))

        div, mod = divmod(num - 1, self.__n)

        if self.state_board[div][mod].get_in_cell():  # проверка, что ячейка не пуста (не пустая строка)
            return False
        else:
            self.state_board[div][mod].set_in_cell(symbol)  # если пуста - поменять на значение символа игрока
            return True

    def check_final(self) -> bool:
        """Метод проверяет условия завершения игровой партии.

        Условия завершения игровой партии: победа одного из игроков - совпадение символов в: ряду, столбце, главной
        диагонали или побочной; ничьй - все ячейки отмечены (заняты символами), но победа не достигнута.
        Условие победы проверяется во вложенной функции: in_check.

        :rtype: bool
        :return: True — если одно из условий выполнилось, False — если нет.
        """

        def in_check(mass: list[list[Cell]]) -> bool:
            """Проверяет факт совпадения значений поля in_cell объектов вложенных списков, пустая строка не считается.

            :param mass: Список вложенных списков объектов класса Cell - 'клетка'.
            :type mass: list[list[Cell]]

            :rtype: bool
            :return: True — элемент списка состоит из одинаковых значений (за исключением пустой строки), False — если нет.
            """

            for lists in mass:
                if len(set(map(lambda x: x.get_in_cell(), lists))) == 1 and lists[0].get_in_cell() != '':
                    return True
            return False

        "проверка условия в функции in_check соответственно: по строкам, по столбцам, по главной диагонали, "
        "по побочной диагонали"
        if any([in_check(self.state_board),
                in_check([list(row) for row in zip(*self.state_board)]),
                in_check([[self.state_board[index][index] for index in range(len(self.state_board))]]),
                in_check([[self.state_board[index][len(self.state_board)-index-1]
                           for index in range(len(self.state_board))]])]):
            return True
        # проверка условия 'ничья' - условия победы не выполнено, но все ячейки не пусты
        elif '' not in set(map(lambda x: x.get_in_cell(), (elem for mas in self.state_board for elem in mas))):
            print('Ничья!')
            return True

        return False


class Player:
    """Класс для представления игроков.

    Может иметь только два объекта класса одновременно.

    Атрибуты
    ________
    name : str
        имя игрока
    wins : int
        количество побед игрока
    symbol : Literal['X'] | Literal['O']
        индивидуальный символ игрока

    Скрытые Атрибуты
    ________________
    __player_symbol : Literal['X', 'O'] = ['X', 'O']
        пул допустимых для всего класса значений символов игроков

    Методы
    ------
    __init__(name: str, symbol: Literal['X', 'O'] = None) -> None
        создаёт атрибуты, присваивает индивидуальные символы
    __del__() -> None
        при удалении игрока, возвращает значение символа в общий пул
    step_play() -> int
        запрашивает у пользователя номер ячейки хода
    """

    name: str
    wins: int
    __player_symbol: Literal['X', 'O'] = ['X', 'O']  # настройка значений по умолчанию
    symbol: Literal['X'] | Literal['O']

    def __init__(self, name: str, symbol: Literal['X', 'O'] = None) -> None:
        """Создаёт атрибуты, распределяет символы по игрокам.

        :param name: Имя игрока
        :type name: str
        :param symbol: Символ игрока, распределяются по умолчанию, но может быть распределён вручную.
        :type symbol: Literal['X', 'O']

        :raise ValueError: При переданном значении поля symbol вне списка принятых значений ['X', 'O'].
        """

        self.name = name
        self.wins = 0  # кол-во побед

        if symbol is None:
            symbol = self.__player_symbol[0]

        self.symbol = symbol  # символ игрока
        assert symbol in self.__player_symbol, 'ValueError: Неверное значение выбранного символа!'
        # удаляем уже использованное значение - следующий игрок может использовать только другое,
        # следовательно, игроков только 2
        self.__player_symbol.remove(symbol)

    def __del__(self) -> None:
        """Деструктор, при удалении объекта-игрока возвращает его символ в общий список.
        """

        if self.symbol in ('X', 'O'):
            self.__player_symbol.append(self.symbol)  # возвращаем значение в пул

    def step_play(self) -> int:
        """Запрашивает номер ячейки у пользователя.

        :rtype: int
        :return: Номер ячейки выбранный игроком для своего хода.
        """

        return int(input("{0} Ваш ход! Выберете номер клетки поля для вашего '{1}': ".format(self.name, self.symbol)))


class Game:
    """Класс для представления игрового процесса.

    Формирует игровой процесс из взаимодействия классов: Board и Player.

    Атрибуты
    ________
    condition_game : Board
        объект класса Board, игровая доска
    gamers : tuple[Player, Player]
        кортеж двух объектов класса Player, игроки

    Методы
    ------
    __init__(condition_game: Board, gamers: tuple[Player, Player]) -> None
        создаёт атрибуты
    show() -> None
        вывод игрового поля на экран
    one_step(player: Player) -> bool
        модуляция одного хода партии
    one_play( -> None
        модуляция одной партии
    play_main() -> None
        стандартный режим запуска, серия игр с подсчётом побед и возможностью выйти после каждой
    """

    condition_game: Board
    gamers: tuple[Player, Player]

    def __init__(self, condition_game: Board, gamers: tuple[Player, Player]) -> None:
        """Конструктор, создаёт поля condition_game, и gamers.

        :param condition_game: Объект класса Board - игровая доска содержащая вложенные списки объектов ячеек.
        :type condition_game: Board
        :param gamers: Игроки
        :type gamers: tuple[Player, Player]
        """

        self.condition_game = condition_game
        self.gamers = gamers

    def show(self) -> None:
        """Вывод игрового поля на экран.

        :return: Вывод на экран
        """

        print('-\t' * (self.condition_game.get_n() * 2 + 1))
        for _, value in enumerate(self.condition_game.state_board):
            for _, elem in enumerate(value):
                print('|', end='\t')
                print('{}'.format(elem.get_in_cell()), end='\t')
            print('|')
            print('-\t' * (self.condition_game.get_n() * 2 + 1))

    def one_step(self, player: Player) -> bool:
        """Метод запуска одного хода игры.

        Получает одного из игроков, запрашивает у игрока номер клетки, изменяет поле, проверяет, выиграл ли игрок.

        :param player: Игрок делающий ход
        :type player: Объект класса Player - игрок, с именем, символом и кол-вом побед.

        :except AssertionError: При значении ячейки превышающем диапазон.
        :except ValueError: При неверном вводе.

        :rtype: bool
        :return: Если игрок победил, возвращает True, иначе False.
        """

        while True:
            try:
                # запрос хода у игрока, проверка клетки на занятость и запись символа игрока если она пуста
                if self.condition_game.change_state_cell(player.step_play(), player.symbol):
                    print('Ход принят.')
                    if self.condition_game.check_final():  # проверка условия окончания партии
                        return True
                    else:
                        return False
                else:
                    print('Ячейка занята! Выберите другую.')

            except AssertionError as err:
                print(err)
            except ValueError as err:
                print(err, 'Пожалуйста число!')

    def one_play(self) -> None:
        """Метод запуска одной игры.

        Очищает поле, запускает цикл с игрой, который завершается победой одного из игроков или ничьей.

        :return: Вывод на экран.
        """

        self.condition_game.__init__(self.condition_game.get_n())  # перезапускает конструктор, для пересоздания ячеек поля
        temp: int = 0
        self.show()

        # очерёдность хода выбирается путём запроса чётного-нечётного игрока (в соответствии с ходом) из списка gamers
        while not self.one_step(self.gamers[temp % 2]):
            temp += 1
            self.show()

        self.show()
        print('Поздравляем победителя: {}!'.format(self.gamers[temp % 2].name))
        self.gamers[temp % 2].wins += 1

    def play_main(self) -> None:
        """Основной метод запуска игр.

        В цикле запускает игры, запрашивая после каждой игры, хотят ли игроки продолжать играть. После каждой игры выводится текущий счёт игроков.

        :return: Вывод на экран.
        """

        flag: bool = True

        while flag:
            self.one_play()
            print('Общий счёт {0} - {1} : {2} - {3}'.format(self.gamers[0].name, self.gamers[0].wins,
                                                            self.gamers[1].name, self.gamers[1].wins,))
            if 'y' != input('\nПродолжить игру? Yes - y; No - любой другой. ').lower():
                print()
                flag = False


try:
    desk = Board()
    A = Player('Tom', 'O')
    B = Player('Vik')
    Game(desk, (A, B)).one_play()

except AssertionError as errors:
    print(errors)
