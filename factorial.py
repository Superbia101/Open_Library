"""факториал числа"""
def fact(n):
    a = 1
    if n > 0:
        for i in range(1,n + 1):
            a = a * i
        print(a)
    else:
        print("Отрицательное - не подходит!")
        
temp=int(input("Ведите число: "))
fact(temp)
