from typing import List, Union


def caesar_cipher(text: str, num: int) -> str:
    """Шифровка переданной строки кодом Цезаря, с заданным сдвигом.

    :param text: Исходный текст
    :type text: str
    :param num: Сдвиг в алфавите
    :type num: int

    :rtype: str
    :return: new_text
    """

    alphabet: List[str] = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    # new_text: str = ''
    # for symbol in text.lower():
    #     if symbol in alphabet:
    #         new_text += alphabet[(alphabet.index(symbol) + num) % len(alphabet)]
    #     else:
    #         new_text += symbol

    new_text: str = ''.join([(alphabet[(alphabet.index(symbol) + num) % len(alphabet)]
                              if symbol in alphabet else symbol) for symbol in text.lower()])

    return new_text


def caesar_cipher_1(text: str, num: int) -> str:
    """Шифровка переданной строки кодом Цезаря, с заданным сдвигом.

    :param text: Исходный текст
    :type text: str
    :param num: Сдвиг в алфавите
    :type num: int
    
    :rtype: str
    :return: Строка из списка text
    """

    alphabet: List[str] = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    text: List[Union[List[str], str]] = [[i] for i in text.lower()]

    for index, symbol in enumerate(text):
        if symbol[0] in alphabet:
            text[index] = alphabet[(alphabet.index(symbol[0]) + num) % len(alphabet)]
        else:
            text[index] = symbol[0]

    return ''.join(text)


if __name__ == "__main__":
    line = input('Введите сообщение: ')
    k_num = int(input('Введите сдвиг: '))
    print('Зашифрованное сообщение:', caesar_cipher(line, k_num))
