def bubble_sorting(list_x):
    "Сортировка методом пузырька в порядке возрастания"
    for _ in range(len(A) + 1 // 2): 
        for i in range(1,len(A)):
            if list_x[i - 1] > list_x[i]:
                list_x[i], list_x[i - 1] = list_x[i - 1], list_x[i]         
    print(list_x)

A = [5, 2, 8, 1, 0, 4, 5, 7, 2, 3, 9, 6, 0]   
bubble_sorting(A)
