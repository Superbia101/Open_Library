def output_degrees_two(num: str) -> None:
    """Выводит необходимое кол-во степеней 2.

    :param num: arg1
    :type num: str

    :return: Выводит на экран
    """
    print("Степени двойки: ",[2 ** i for i in range(int(num))])


temp = input("Ведите кол-во: ")
output_degrees_two(temp)
#print("Степени двойки: ",[2**i for i in range(int(input("Ведите кол-во: ")))])
