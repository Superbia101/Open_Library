"""интервал чисел с 3-мя условиями: делится без остатка,
с остатком и сумма цифр < 10. по умолчанию создаёт нечётные от 0 до 1000"""

def Myfunk(A=0,B=1000,C=1,D=2):
    "Числа от A до B, %C==0 and %D!=0 and sum цифр в которых меньше десяти"
    a=[sum([int(str(i)[j]) for j in range(len(str(i)))])<10 and i for i in range(A,B+1,C) if i%D!=0] #список чисел с 3-мя услов, но лишними False
    for i in range(a.count(False)): # удаляем лишние False
        a.remove(False)
    print(*a)
Myfunk()
