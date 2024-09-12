print('Загадайте число от 1 до 100')
print('Оттвечайте на запросы компьтера: 1 - равно, 2 - больше, 3 - меньше')
print('Начали!', end = '\n\n')
low_limit, big_limit = 0, 100
while True:
  middle = (low_limit + big_limit) // 2
  print('Твое число равно, меньше или больше, чем число', str(middle) + '?')
  num = int(input())
  if num == 1:
    break
  elif num == 2:
    low_limit = middle
  else:
    big_limit = middle  
print('Число равно:', limit, '!')
