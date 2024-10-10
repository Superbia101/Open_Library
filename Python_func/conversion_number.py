def conversion_number(num: int, quant: int) -> str:
    """Переводит число в необходимую систему счисления до 36-й.

    :param num: arg1
    :type num: int
    :param quant: arg2
    :type quant: int

    :raises ValueError: quant > 36

    :rtype: str
    :return: new_num
    """
    if quant > 36:
        raise ValueError('Ошибка! Недопустимая система счисления.')

    new_num: str = ""

    while num > 0:
        num, rem = divmod(num, quant)
        rem = chr(ord('A') - 10 + rem) if rem > 9 else rem
        new_num = str(rem) + new_num

    return new_num


a: int = int(input('Число: '))
b: int = int(input('Основание системы счисления: '))
print(conversion_number(a, b))
