#print("Степени двойки: ",[2**i for i in range(int(input("Ведите кол-во: ")))])

"""функция"""
def degrees(num):
    "Выводит необходимое кол-во степеней 2"
    print("Степени двойки: ",[2**i for i in range(int(num))])
temp = input("Ведите кол-во: ")
degrees(temp)
