def count_letters_and_nums(txt: str) -> None:
    """Поиск и подсчёт буквы и цифры в тексте.

    :param txt: Текст
    :type txt: str

    :return: Выводит результат на экран
    """

    num = input('Какую цифру ищем? ')
    symbol = input('Какую букву ищём? ')
    ind_num: int = 0
    ind_symbol: int = 0

    for elem in txt:
        ind_num += 1 if elem == num else 0
        ind_symbol += 1 if elem == symbol else 0

    print(f'\nКоличество цифр {num}:', ind_num)
    print(f'Количество букв {symbol}:', ind_symbol)


if __name__ == "__main__":
    count_letters_and_nums(input('Введите текст: '))
