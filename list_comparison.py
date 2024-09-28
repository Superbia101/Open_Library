def list_comparison(list_1: list[int], list_2: list[int]):
    """сравниваются (на предмет равенства) два числовых списка"""
    x: int = 0
    if len(list_1) == len(list_2): # сравнивается длина
        for i in range(len(list_1)):
            x= x + 1 if (list_1[i] == list_2[i]) else x + 0 # подсчёт одинаковых элементов
        if x == len(list_1): # проверка кол-ва эл.
            print("Равны!")
        else:
            print("Не равны!")
    else:
        print("Не равны!")




a = [1, 2, 0, 6]
b = [1, 2, 5, 6]
list_comparison(a, b)
