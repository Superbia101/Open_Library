from random import *




def my_list(line: int, column: int):
    """cоздаёт и выводит вложеный список n на m, заполн. случ. буквами"""
    seed(2024)
    rand_list: list[list[int | str]] = [[0] * column for _ in range(line)]
    for i in range(line):
        for j in range(column):
            rand_list[i][j] = chr(randint(ord('A'), ord('Z')))
    for row in rand_list:
        print(' '.join(row))




n, m = 4, 4
my_list(n, m)
