def output_factorial(num: int) -> None:
    """Факториал числа.

    :param num: arg1
    :type num: int

    :return: Выводит на экран
    """
    comp: int = 1

    if num > 0:
        for i in range(1, num + 1):
            comp *= i
        print('Факториал числа', num, 'равен', comp)
    else:
        print("Отрицательное - не подходит!")


temp = int(input("Введите число: "))
output_factorial(temp)
