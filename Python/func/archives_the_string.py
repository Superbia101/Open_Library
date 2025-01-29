def archives_the_string(text: str) -> str:
    """Принимает и кодирует строку, заменяя символы их количеством.

    :param text: Исходная строка
    :type text: str

    :rtype: str
    :return: new_text - закодирована строка
    """

    count: int = 0
    new_text: str = ''
    
    for index, symbol in enumerate(text):
        count += 1
        
        if index == len(text) - 1 or symbol != text[index + 1]:
            new_text += '{0}{1}'.format(symbol, count)
            count = 0
            
    return new_text


if __name__ == "__main__":
    txt = input('Введите строку: ')
    #txt = 'aaAAbbсaaaA'
    print('Закодированная строка:', archives_the_string(txt))
