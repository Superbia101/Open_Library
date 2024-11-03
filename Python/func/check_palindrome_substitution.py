def check_palindrome_substitution(txt: str) -> None:
    """Определяет, существует ли у переданной строки такая перестановка,
    при которой она станет палиндромом.

    :param txt: arg1
    :type txt: str
    :return: Выводит на экран
    """
    count_odd: int = 0
    len_text: int = len(txt)
    dict_origin: dict[str:int] = dict((symbol, txt.count(symbol)) for symbol in txt)

    for val in dict_origin.values():
        count_odd += 1 if val % 2 != 0 else 0
        if count_odd > 0 and len_text % 2 == 0 or count_odd > 1 and len_text % 2 != 0:
            print('Нельзя сделать палиндромом')
            break
    else:
        print('Можно сделать палиндромом')


check_palindrome_substitution(input('Введите строку: '))
