from typing import Final
from random import choices


def creation_class(source: type, name_list: list[str]) -> list[type]:
    """Создаёт производные классы в количестве переданных имён из списка. Имеет встроенную функцию - метод для классов.

    :param source: Базовый класс
    :type source: type
    :param name_list: Список имен новых классов
    :type name_list: list[str]

    :rtype: list[type]
    :return: Список производных классов с соответствующими именами
    """

    def __str__(self) -> str:
        """Строковое представление.

        :rtype: str
        :return: Имя класса
        """
        return self.__class__.__name__

    return [type(name, (source,), {'__str__': __str__}) for name in name_list]

def one_day(errs: list[type]) -> int:
    """Возвращает количество кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из исключений.

    :raise KillError, DrunkError, CarCrashError, GluttonyError, DepressionError: С вероятностью 1/10

    :rtype: int
    :return: Число от 1 до 7
    """

    if choices([True, False], [1/10, 9/10])[0]:
        raise choices(errs)[0]

    return choices(range(1, 8))[0]


err_name: list[str] = ['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError']
err_list: list[type] = creation_class(Exception, err_name)

LIMIT_KARMA: Final[int] = 500
karma: int = 0
day: int = 0

with open('karma.log', 'w', encoding='utf-8') as karma_log:
    while karma < LIMIT_KARMA:
        try:
            day += 1
            karma += one_day(err_list)

        except (err_list[0], err_list[1], err_list[2], err_list[3], err_list[4]) as err:
            karma_log.write('День № {0}. Произошло: {1}.\n'.format(day, err))

    karma_log.write('Достигнуто просветление!')
