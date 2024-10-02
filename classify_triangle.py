def classify_triangle(string: str) -> str:
    """Проверяет существование треугольника с введёнными сторонами, считает его площадь.

    :param string: arg1
    :type string: str

    :rtype: str
    :return: Строку, содержащую area
    """
    string = [int(i) for i in string.split()]
    for i in range(-1, 2):
        if not(string[0 - i] + string[1 - i] > string[-1 - i]):
            return 'Не существует'
    p: float = (string[0] + string[1] + string[2]) / 2
    area: float = (p * (p - string[0]) * (p - string[1]) * (p - string[2])) ** 0.5
    return f'Площадь треугольника: {round(area, 2)}'


nums = input('Введите три стороны возможного треугольника, через пробел: ')
print(classify_triangle(nums))
