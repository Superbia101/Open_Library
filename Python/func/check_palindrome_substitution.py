from collections import Counter
from typing import Dict


def can_be_poly(line: str) -> bool:
    """Функция принимает на вход строку и проверяет, можно ли путём перестановок получить из неё палиндром.

    :param line: Переданная на проверку строка
    :type line: str

    :rtype: bool
    :return: True - может быть палиндромом, False - нет.
    """

    return sum(map(lambda x: x % 2, Counter(line).values())) <= 1


def check_palindrome_substitution(txt: str) -> None:
    """Определяет, существует ли у переданной строки такая перестановка, при которой она станет палиндромом.

    :param txt: Переданная строка
    :type txt: str
    """
    
    count_odd: int = 0
    len_text: int = len(txt)
    dict_origin: Dict[str:int] = dict((symbol, txt.count(symbol)) for symbol in txt)

    for val in dict_origin.values():
        count_odd += 1 if val % 2 != 0 else 0

        if count_odd > 0 and len_text % 2 == 0 or count_odd > 1 and len_text % 2 != 0:
            print('Нельзя сделать палиндромом')
            break

    else:
        print('Можно сделать палиндромом')


if __name__ == '__main__':
    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))
    check_palindrome_substitution(input('Введите строку: '))
