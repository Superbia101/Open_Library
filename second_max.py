def second_max(list_num: list[int | float], first: bool = False) -> list[int | float]:
    """функция возвращает первый/второй максимум и его индекс из переданного списка"""
    if first: # если функции передан второй аргумент - возвращает второй макс
        list_num.remove(max(list_num))
    return [max(list_num), list_num.index(max(list_num))]

def second_max_modified(list_num: list | tuple) -> list[tuple]:
    """функция возвращает первый и второй максимум и, их индексы из списка"""
    first, second = list_num[:2] # берём первое и второе значение из списка
    f_index, s_index = 0, 1 # значения индексов 
    if first < second: # распределяем их
        first, second = second, first
        f_index, s_index = 1, 0
    for i in range(2, len(list_num)): # сравниваем все значения с 1-вым макс
        if first < list_num[i]:
            first, second = list_num[i], first # заменяем на большие
            f_index, s_index = i, f_index # их индексы тоже
        elif second < list_num[i]: # сравниваем 2-той
            second = list_num[i]
            s_index = i
    return [(first, f_index), (second, s_index)]

a: list[int] = [1, 2, 3, 4, 5, 23, 6, 7, 3, 89, 4]
#print(*second_max(a,1))
print(second_max_modified(a))
