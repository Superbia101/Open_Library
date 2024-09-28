def output_factorial(num: int):
    """факториал числа"""
    comp: int = 1
    if num > 0:
        for i in range(1, num + 1):
            comp *= i
        print('Факторил числа', num, 'равен', comp)
    else:
        print("Отрицательное - не подходит!")




temp = int(input("Введите число: "))
output_factorial(temp)
