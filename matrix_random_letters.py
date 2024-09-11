from random import *  
def my_list(n, m):
    "Создаёт и выводит вложеный список n на m, заполн. случ. буквами"
    a = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            a[i][j] = chr(randint(ord('A'), ord('Z')))
    for row in a:
        print(' '.join(row))
n, m = 4, 4
seed(2024)
my_list(n, m)
