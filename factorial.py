def fact(num):
    "Факториал числа"
  comp = 1
  if num > 0:
      for i in range(1, num + 1):
          comp *= i
      print('Факторил числа', num, 'равен', comp)
  else:
      print("Отрицательное - не подходит!")

temp = int(input("Введите число: "))
fact(temp)
