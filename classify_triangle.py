def classify_triangle(input_string: str)-> str:
    """Проверяет существует ли треугольник с введёнными сторонами, считает площадь"""
    input_string = [int(i) for i in input_string.split()]

    for i in range(-1,2):
        if not(input_string[0 - i] + input_string[1 - i] > input_string[-1 - i]):
            return 'Не существует'
            break
    else:
        p = (input_string[0] +input_string[1] + input_string[2]) / 2
        area = (p * (p - input_string[0]) * (p - input_string[1]) * (p - input_string[2])) ** 0.5
    return round(area, 2)

input_string = input('Введите три стороны возможного треугольника, через пробел: ')
temp = classify_triangle(input_string)
print(temp
