def dict_freq(text: str) -> dict[str: int]:
    """Создаёт из переданной строки словарь частот символов.

    :param text: arg1
    :type text: str

    :rtype: dict[str:int]
    :return: dict_count
    """
    dict_count: dict[str: int] = {}

    for symbol in text:
        dict_count[symbol] = dict_count.get(symbol, 0) + 1

    return dict_count


def dict_freq_invert(diction: dict[str:int]) -> dict[int: list[str]]:
    """Создаёт из переданного словаря инвертированный по отношению ключ - значение.

    :param diction: arg1
    :type diction: dict[str:int]

    :rtype: dict[int: list[str]]
    :return: dict_invert
    """
    dict_invert: dict[int: list[str]] = {}

    for keys, value in diction.items():
        dict_invert[value] = dict_invert.get(value, []) + [keys]

    return dict_invert


def dict_print(glossary: dict) -> None:
    """Выводит на экран элементы переданного словаря.

    :param glossary: arg1
    :type glossary: dict

    :return: Выводит на экран
    """
    for key, val in glossary.items():
        print('{} : {}'.format(key, val))




txt = input('Введите текст: ')

dict_origin: dict[str: int] = dict_freq(txt)
# dict_origin: dict[str:int] = dict((symbol, txt.count(symbol)) for symbol in txt)

print('Оригинальный словарь частот:', end='\n\n')
dict_print(dict_origin)

dict_result: dict[int: list[str]] = dict_freq_invert(dict_origin)

print('\nИнвертированный словарь частот:')
dict_print(dict_result)
