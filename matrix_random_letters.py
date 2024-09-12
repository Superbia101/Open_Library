from random import *  
def my_list(line, column):
    "Создаёт и выводит вложеный список n на m, заполн. случ. буквами"
    a = [[0] * column for i in range(line)]
    for i in range(line):
        for j in range(column):
            a[i][j] = chr(randint(ord('A'), ord('Z')))
    for row in a:
        print(' '.join(row))
n, m = 4, 4
seed(2024)
my_list(n, m)
