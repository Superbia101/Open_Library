def count_letters(text):
    """Поиск и подсчёт буквы и цифры в тексте"""
  num = input('Какую цифру ищем? ')
  symbol = input('Какую букву ищём? ')
  ind_num, ind_symbol = 0, 0
  for elem in text:
    ind_num += 1 if elem == num else 0
    ind_symbol += 1 if elem == symbol else 0
  print(f'\nКоличество цифр {num}:', ind_num)
  print(f'Количество букв {symbol}:', ind_symbol)

count_letters(input('Введите текст: '))
