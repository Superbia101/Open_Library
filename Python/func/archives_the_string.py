def archives_the_string(text: str) -> str:
    """Принимает и кодирует строку, заменяя символы их количеством.

    :param text: arg1
    :type text: str

    :rtype: str
    :return: new_text
    """
    count: int = 0
    new_text: str = ''
    
    for index, symbol in enumerate(text):
        count += 1
        
        if index == len(text) - 1 or symbol != text[index + 1]:
            new_text += f'{symbol}{count}'
            count = 0
            
    return new_text


txt = input('Введите строку: ')
#txt = 'aaAAbbсaaaA'
print('Закодированная строка:', archives_the_string(txt))
