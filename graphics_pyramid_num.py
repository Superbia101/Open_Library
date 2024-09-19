def pyramid_num():
    """выводит на экран заполненную нечётными числами пирамиду"""
    num = int(input('Введите высоту пирамиды: '))
    print()
    temp = 1

    for row in range(1, num + 1):
      for col in range(1, 2 * num):
        if num + 2 * row > row + col > num and row % 2 == col % 2:
          print(temp, end = ' ')
          temp += 2
        else:
          print(end = '   ')
      print()

pyramid_num()
