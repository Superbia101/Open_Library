def VtorMax(A):
    "Функция возвращает второй максимум из списка"
    A.remove(max(A))
    return max(a)

a=[1,2,3,4,5,23,6,7,3,89,4]
print(VtorMax(a))
