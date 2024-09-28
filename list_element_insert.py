from random import *




def element_insert(num: int):
    """между каждой парой элем. списка заданной длины вставляется новый, равный сумме соседних"""
    seed(2024)
    list_1: list[int] = [randint(0, 9) for _ in range(num)] # создаём случ. список
    print('Случайный список:', list_1)
    list_2: list[int] = list_1[:] # поверхностная копия
    temp: int = 1 # поправка на сдвиг
    for i in range(len(list_1) - 1):
        list_2[i + temp:i + temp] = [list_1[i] + list_1[i + 1]]
        temp += 1
    print('Результат:', list_2)




element_insert(10)
