from random import *  
def element_insert(num):
    "между каждой парой элем. списка вставляется новый, равный сумме соседних"
    seed(2024)
    A = [randint(0, 9) for _ in range(num)] # создаём случ. список
    print('Случайный список:', A)
    B = A[:] # поверхностная копия
    temp = 1 # поправка на сдвиг
    for i in range(len(A) - 1):
        B[i + temp:i + temp] = [A[i] + A[i + 1]]
        temp += 1
    print('Результат:', B)

element_insert(10)
