def list_comparison(a,b):
    "сравниваются (на предмет равенства) два числовых списка"
    x = 0
    if len(a) == len(b): # сравнивается длина
        for i in range(len(a)):
            x= x + 1 if (a[i] == b[i]) else x + 0 # подсчёт одинаковых элементов
        if x == len(a): # проверка кол-ва эл.
            print("Равны!")
        else:
            print("Не равны!")
    else:
        print("Не равны!")

a = [1, 2, 0, 6]
b = [1, 2, 5, 6]
list_comparison(a,b)
