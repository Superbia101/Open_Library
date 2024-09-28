def node_euclid_algorithm(num_1: int, num_2: int):
    """поиск наибольшего общего делителя, через алгоритм Евклида"""
    num_1, num_2 = max(num_1, num_2), min(num_1, num_2)
    while num_1 % num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    print('НОД двух чисел:', num_2)




node_euclid_algorithm(int(input('Введите 1-е число: ')),
                    int(input('Введите 2-е число: ')))
#print('НОД двух чисел:', gcd(num_1, num_2)) # проверка результата
