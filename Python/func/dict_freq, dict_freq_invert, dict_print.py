from typing import Dict, List


def dict_freq(text: str) -> Dict[str: int]:
    """Создаёт из переданной строки словарь частот символов.

    :param text: Строка
    :type text: str

    :rtype: Dict[str:int]
    :return: dict_count
    """

    dict_count: Dict[str: int] = {}

    for symbol in text:
        dict_count[symbol] = dict_count.get(symbol, 0) + 1

    return dict_count


def dict_freq_invert(diction: Dict[str:int]) -> Dict[int: List[str]]:
    """Создаёт из переданного словаря инвертированный по отношению ключ - значение.

    :param diction: Словарь
    :type diction: Dict[str:int]

    :rtype: Dict[int: List[str]]
    :return: dict_invert
    """

    dict_invert: Dict[int: List[str]] = {}

    for keys, value in diction.items():
        dict_invert[value] = dict_invert.get(value, []) + [keys]

    return dict_invert


def dict_print(glossary: dict) -> None:
    """Выводит на экран элементы переданного словаря.

    :param glossary: Словарь
    :type glossary: dict

    :return: Выводит на экран
    """

    for key, val in glossary.items():
        print('{} : {}'.format(key, val))


if __name__ == "__main__":
    txt = input('Введите текст: ')

    dict_origin: dict[str: int] = dict_freq(txt)
    # dict_origin: dict[str:int] = dict((symbol, txt.count(symbol)) for symbol in txt)

    print('Оригинальный словарь частот:', end='\n\n')
    dict_print(dict_origin)

    dict_result: dict[int: list[str]] = dict_freq_invert(dict_origin)

    print('\nИнвертированный словарь частот:')
    dict_print(dict_result)
