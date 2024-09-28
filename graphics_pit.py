def pit():
    """получает на вход число N и выводит на экран числа в виде ямы"""
    num = int(input('Введите число N: '))
    print()
    for row in range(1, num + 1):
      for col in range(1, 2 * num + 1):
        temp = num + 1 - col if col <= num else col - num 
        if row - col >= 0 or col + row >= 2 * num + 1:
          print(temp, end = '')
        else:
          print('.', end = '')
      print()




pit()
