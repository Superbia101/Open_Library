"""Жадные алгоритмы"""
from typing import Dict


def huffman_decoding(msg: str, symbol_dict: Dict[str, str]) -> str:
    """Функция восстанавливает зашифрованную кодом Хаффмана строку по беспрефиксному коду символов.

    :param msg: Зашифрованная строка
    :type msg: str
    :param symbol_dict: Словарь, кодов-ключей
    :type symbol_dict: Dict[str, str]

    :rtype: str
    :return: Расшифрованная строка
    """

    result = []
    num_symbol = 0

    while num_symbol < len(msg):
        for key, val in symbol_dict.items():
            if msg.startswith(val, num_symbol):
                result.append(key)
                num_symbol += len(val)
                break
        else:
            print('Что-то не так!')
            break

    return ''.join(result)


# num, len_str = map(lambda x: int(x), input().split(' '))
# cod_dict = {}
#
# for _ in range(num):
#     symbol, code = input().split(': ')
#     cod_dict[symbol] = code
#
# text = input()

text = '01001100100111'
cod_dict = {"a": "0", "b": "10", "c": "110", "d": "111"}
print(huffman_decoding(text, cod_dict))
