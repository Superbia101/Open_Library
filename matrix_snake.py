def snake(line, column):
    "Создаёт и выводит матрицу заполненную числами по спирали"
    A = [[0] * column for i in range(line)]
    num, temp, i, j = 0, 0, 0, 0 
    while num < line * column: 
        for j in range(temp, column - temp): # заполн. верхнего октанта
            if A[i][j] == 0:
                num += 1
                A[i][j] = num
        for i in range(temp, line - temp): # заполн. левого октанта
            if A[i][j] == 0:
                num += 1
                A[i][j] = num
        for j in range(column - 1 - temp, temp - 1, -1): # заполн. нижнего окт.
            if A[i][j] == 0:
                num += 1
                A[i][j] = num
        for i in range(line - 1 - temp, temp, -1): # заполн. правого окт.
            if A[i][j] == 0:
                num += 1
                A[i][j] = num        
        temp += 1 # переход на след. куруг
    print('Матрица - "змейка"!')
    for row in A:
        print(' '.join([str(elem) for elem in row]))


n, m = int(input('Введите кол-во строк: ')), int(input('Введите кол-во столбцов: '))
print()
snake(n, m)

