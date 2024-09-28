def count_letters_and_nums(txt: str):
    """поиск и подсчёт буквы и цифры в тексте"""
    num: str = input('Какую цифру ищем? ')
    symbol: str = input('Какую букву ищём? ')
    ind_num: int = 0
    ind_symbol: int = 0
    for elem in txt:
      ind_num += 1 if elem == num else 0
      ind_symbol += 1 if elem == symbol else 0
    print(f'\nКоличество цифр {num}:', ind_num)
    print(f'Количество букв {symbol}:', ind_symbol)




count_letters_and_nums(input('Введите текст: '))
