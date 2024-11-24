"""Жадные алгоритмы"""

def points_on_segments() -> None:
    """Функция находит минимальное множество точек, которые лежат на всех заданных отрезках.
    """
    
    num_list = []
    value = []

    for _ in range(int(input('Кол-во отрезков: '))):
        num_list.append([int(i) for i in input('l r: ').split(' ')])

    num_list.sort(key=lambda x: x[1])
    elem: list[int] = num_list[0]

    for i in range(1, len(num_list)):
        if elem[1] < num_list[i][0]:
            value.append(str(elem[1]))
            elem = num_list[i]
            
        if len(num_list) == i + 1:
            value.append(str(elem[1]))
            
    print(len(value))        
    print(' '.join(value))


points_on_segments()
