from random import *




def matrix_redact(line: int, column: int, re_line: int, re_column: int):
    """cоздаёт и выводит вложеный список n на m, у котор. удаляется опред строка и столбец"""
    seed(2024)
    rand_list: list[list[int]] = [[randint(0, 9) for _ in range(column)] for _ in range(line)] # создаётся матрица случайных значений
    for row in rand_list: # демонстрация результата
        print(' '.join([str(elem) for elem in row]))
    print()
    rand_list.pop(re_line) # удаляем строку
    for i in range(len(rand_list)): # удаляем столбец
        rand_list[i].pop(re_column)
    for row in rand_list: # демонстрация результата
        print(' '.join([str(elem) for elem in row]))




matrix_redact(5, 7, 3, 3)
