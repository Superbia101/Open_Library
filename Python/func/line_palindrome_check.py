def line_palindrome_check(lines: str) -> bool:
    """Проверяет строку, является ли она палиндромом.

    :param lines: arg1
    :type lines: str

    :rtype: bool
    :return: True - строка палиндром, False - строка не палиндром
    """

    text: str = ''
    temp: int = 0

    for j in lines.lower().split():  # Убираем лишнее
        text += j.strip(".,:;-!?")
    for i in range(len(text) // 2):  # Подсчёт одинаковых значений с начала и конца
        temp += 1 if text[i] == text[len(text) - 1 - i] else 0

    return temp == len(text) // 2


if __name__ == '__main__':
    #t = input('Введите строку: ')
    #t = 'казак'
    t = ' Я не стар, брат Сеня!'
    print(t)
    print(line_palindrome_check(t))
