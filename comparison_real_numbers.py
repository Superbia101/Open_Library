def comparison_real_numbers(namber_sum_1: float, namber_sum_2: float, namber_raz: float):
    """сравн. сумму двух вещ. чисел с третьим с точностью: до 15-го знака"""
    print('\n', abs((namber_sum_1 + namber_sum_2) - namber_raz) < 1e-15)




num = 1.1
num_2 = 2.2
num_3 = 3.3
#num = float(input('Введите первое число: '))
#num_2 = float(input('Введите второе число: '))
#num_3 = float(input('Введите третье число: '))
comparison_real_numbers(num, num_2, num_3)
