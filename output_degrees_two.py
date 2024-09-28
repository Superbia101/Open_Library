def output_degrees_two(num: str):
    """выводит необходимое кол-во степеней 2"""
    print("Степени двойки: ",[2 ** i for i in range(int(num))])




temp = input("Ведите кол-во: ")
output_degrees_two(temp)
#print("Степени двойки: ",[2**i for i in range(int(input("Ведите кол-во: ")))])