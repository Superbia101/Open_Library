def second_max(A):
    "Функция возвращает второй максимум из списка"
    A.remove(max(A))
    return max(a)

def second_max_modified(A):
    "Функция возвращает второй максимум из списка"
    first, second = A[:2]
    if first < second:
        first, second = second, first
    for i in A[2:]:
        if first < i:
            first, second = i, first
        elif second < i:
            second = i
    return (first, second)

a=[1,2,3,4,5,23,6,7,3,89,4]
print(second_max_modified(a))
