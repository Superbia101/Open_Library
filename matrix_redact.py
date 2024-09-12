from random import *  
def matrix_redact(line, column, re_line, re_column):
    "Создаёт и выводит вложеный список n на m, у котор. удаляется опред строка и столбец"
    seed(2024)
    A = [[randint(0, 9) for j in range(column)] for i in range(line)] # создаётся матрица случайных значений
    for row in A: # демонстрация результата
        print(' '.join([str(elem) for elem in row]))
    print()
    A.pop(re_line) # удаляем строку
    for i in range(len(A)): # удаляем столбец
        A[i].pop(re_column)
    for row in A: # демонстрация результата
        print(' '.join([str(elem) for elem in row]))
        
matrix_redact(5, 7, 3, 3)
