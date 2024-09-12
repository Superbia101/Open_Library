from random import *  
def sort_special(num):
    "создаёт случ список и преобразовывает в перемежающуюся последовательность"
    seed(2024)
    A = [randint(0, 9) for _ in range(num)] # создаём случ. список
    print('Случайный список:', A)
    even = sorted(A[0::2])
    uneven = sorted(A[1::2], reverse = True)
    print('Чётные эл. по возрастанию:', even)
    print('Нечётные по убыванию', uneven)
    B, i = [], 0
    while len(B) < len(A):
        B.append(even[i])
        B.append(uneven[i])
        i += 1
    print('Итоговый список:', B)

sort_special(20)
    
