def sum_multiplic_list(list_1, list_2):
    """ сумма попарных произведений элементов списков"""
    if len(list_1) != len(list_2):
        if len(list_1) < len(list_2):
            list_1, list_2 = list_2, list_1
            
        item = 0
        while len(list_1) != len(list_2):
            list_2.append(list_2[item])
            item += 1
            
    return sum([symbol * list_2[index] for index, symbol in enumerate(list_1)])

#A = [1, 2, 3, 4, 5, 6]
#B = [0, 7, 8]
A = [1, 0, 1]
B = [i for i in range(30)]
print(sum_multiplic_list(A, B))
