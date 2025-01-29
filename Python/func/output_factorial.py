def output_factorial(num: int) -> None:
    """Факториал переданного числа выводится на экран.

    :param num: Число
    :type num: int

    :return: None
    """

    comp: int = 1

    if num > 0:
        for i in range(1, num + 1):
            comp *= i
        print('Факториал числа', num, 'равен', comp)
    else:
        print("Отрицательное - не подходит!")

if __name__ == "__main__":
    temp = int(input("Введите число: "))
    output_factorial(temp)
