def caesar_cipher(text: str, num: int) -> str:
    """Шифровка переданной строки кодом Цезаря, с заданным сдвигом.

    :param text: arg1
    :type text: str
    :param num: arg2
    :type num: int
    
    :rtype: str
    :return: new_text
    """
    alphabet: list[str] = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    # new_text: str = ''
    # for symbol in text.lower():
    #     if symbol in alphabet:
    #         new_text += alphabet[(alphabet.index(symbol) + num) % len(alphabet)]
    #     else:
    #         new_text += symbol

    new_text: str = ''.join([(alphabet[(alphabet.index(symbol) + num) % len(alphabet)]
                         if symbol in alphabet else symbol) for symbol in text.lower()])
    return new_text


line = input('Введите сообщение: ')
k_num = int(input('Введите сдвиг: '))
print('Зашифрованное сообщение:', caesar_cipher(line, k_num))
