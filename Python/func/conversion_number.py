def conversion_number(num: int, quant: int) -> str:
    """Переводит число в необходимую систему счисления до 36-й.

    :param num: Число
    :type num: int
    :param quant: Система счисления до 36
    :type quant: int

    :raises ValueError: quant > 36

    :rtype: str
    :return: То же число в заданной системе
    """

    if quant > 36:
        raise ValueError('Ошибка! Недопустимая система счисления.')

    new_num: str = ""

    while num > 0:
        num, rem = divmod(num, quant)
        rem = chr(ord('A') - 10 + rem) if rem > 9 else rem
        new_num = str(rem) + new_num

    return new_num


if __name__ == "__main__":
    a: int = int(input('Число: '))
    b: int = int(input('Основание системы счисления: '))
    print(conversion_number(a, b))
