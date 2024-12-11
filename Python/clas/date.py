from __future__ import annotations
from datetime import datetime as dt
from typing import Union
import re


class Date:
    """
    Класс для проверки формата и вывода даты.

    Атрибуты
    ________
    PATTERN
        Константа класса, содержит образец сравнения входящих строк, в форме регулярных выражений

    Методы
    ________
    is_date_valid(date_str : str) -> bool
        Классовый метод проверяет числа даты на корректность
    from_string(date_str : str) -> Union[Date, bool]
        Классовый метод возвращает объект класса Date с данными даты
    """

    PATTERN = re.compile(r"\d{1,2}-\d{1,2}-\d{4}")

    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return 'День: {0}\tМесяц: {1}\tГод: {2}'.format(self.day, self.month, self.year)

    @classmethod
    def is_date_valid(cls, date_str: str) -> bool:
        """Классовый метод проверяет числа даты на корректность

        :param date_str: Проверяемая строка формата дд-мм-гггг
        :type date_str: str

        :except ValueError: Такая дата не может существовать

        :rtype: bool
        :return: True - строка может быть датой, False - нет.
        """

        if not cls.PATTERN.match(date_str):
            print('Не верный формат ввода. Пример: "дд-мм-гггг".')
            return False

        try:
            dt.strptime(date_str, '%d-%m-%Y')
        except ValueError:
            return False

        return True

    @classmethod
    def from_string(cls, date_str: str) -> Union[Date, bool]:
        """Классовый метод возвращает объект класса Date с данными даты.

        :param date_str: Строка формата дд-мм-гггг
        :type date_str: str

        :rtype: Union[Date, bool]
        :return: Объект Date, или False - если это не может быть датой
        """

        if cls.is_date_valid(date_str):
            year, month, day = str(dt.strptime(date_str, '%d-%m-%Y').date()).split('-')
            return Date(day=int(day), month=int(month), year=int(year))

        return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
