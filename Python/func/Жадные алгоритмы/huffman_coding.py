"""Жадные алгоритмы"""
from __future__ import annotations
from typing import Optional


class TreeNode:
    """
    Класс элемента бинарного дерева.

    Атрибуты
    ________
    value : int
        вес элемента
    symbol : Optional[str]
        кодируемый символ
    left : Optional[TreeNode]
        левая ветка
    right : Optional[TreeNode]
        правая ветка
    """

    value: int
    symbol: Optional[str]
    left: Optional[TreeNode]
    right: Optional[TreeNode]

    def __init__(self, value: int,
                 symbol: Optional[str] = None,
                 left: Optional[TreeNode] = None,
                 right: Optional[TreeNode] = None) -> None:
        self.value = value
        self.symbol = symbol
        self.left = left
        self.right = right


def huffman_coding(msg: str) -> TreeNode:
    """Функция формирует бинарное дерево для выполнения кодирования переданной строки по методу Хаффмана.

    :param msg: Кодируемая строка
    :type msg: str

    :rtype: TreeNode
    :return: Корень бинарного дерева
    """

    symbol_dict = {i: msg.count(i) for i in set(msg)}

    symbol_dict = sorted(symbol_dict.items(), key=lambda x: x[1])
    sheet_list = [TreeNode(j, i) for i, j in symbol_dict]

    while len(sheet_list) != 1:
        left: TreeNode = sheet_list.pop(1)
        right: TreeNode = sheet_list.pop(0)
        elem: TreeNode = TreeNode(value=(left.value + right.value), left=left, right=right)
        sheet_list.append(elem)
        sheet_list = sorted(sheet_list, key=lambda x: x.value)

    return sheet_list[0]


def encode(node: TreeNode, s: str, huffman_code: dict[str: str]) -> None:
    """Функция заполняет переданный словарь кодировками символов по методу Хаффмана.

    :param node: Корень бинарного дерева
    :type node: TreeNode
    :param s: Строка
    :type s: str
    :param huffman_code: Заполняемый словарь
    :type huffman_code: dict[str: str]
    """

    if node is None:
        return

    # листовой узел
    if node.left is None and node.right is None:
        huffman_code[node.symbol] = s if len(s) > 0 else '1'

    encode(node.left, '{}1'.format(s), huffman_code)
    encode(node.right, '{}0'.format(s), huffman_code)


text = 'abacabad'

if len(text) > 1:
    code_symbol = {}
    encode(huffman_coding(text), '', code_symbol)
else:
    code_symbol = {text: '0'}

code_text = ''

for k in text:
    code_text += code_symbol.get(k)

print(len(code_symbol), len(code_text))

for key, val in sorted(code_symbol.items()):
    print('{0}: {1}'.format(key, val))

print(code_text)
