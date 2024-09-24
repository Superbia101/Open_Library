def comparison_real_numbers(num: float, num_2: float, num_3: float):
    """сравн. сумму двух вещ. чисел с третьим с точностью: до 15-го знака"""
    print('\n', abs((num + num_2) - num_3) < 1e-15)

num = 1.1
num_2 = 2.2
num_3 = 3.3
#num = float(input('Введите первое число: '))
#num_2 = float(input('Введите второе число: '))
#num_3 = float(input('Введите третье число: '))
comparison_real_numbers(num, num_2, num_3)
