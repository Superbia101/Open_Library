def second_max(A, first = False):
    "Функция возвращает первый/второй максимум и его индекс из переданного списка"
    if first: # если функции передан второй аргумент - возвращает второй макс
        A.remove(max(A))
    return [max(A), A.index(max(A))]

def second_max_modified(A):
    "Функция возвращает первый и второй максимум и, их индексы из списка"
    first, second = A[ : 2 ]
    f_index, s_index = 0, 1 # значения индексов 
    if first < second:
        first, second = second, first
        f_index, s_index = 1, 0
    for i in range(2, len(A)):
        if first < A[i]:
            first, second = A[i], first
            f_index, s_index = i, f_index
        elif second < A[i]:
            second = A[i]
            s_index = i
    return [(first, f_index), (second, s_index)]

a=[1, 2, 3, 4, 5, 23, 6, 7, 3, 89, 4]
#print(*second_max(a,1))
print(second_max_modified(a))
