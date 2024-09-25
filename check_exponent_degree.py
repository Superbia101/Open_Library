import math

def exponent_degree(quant: float)-> list:
    """определяет значение степени экспоненциального представления числа"""
    count = 0
    if abs(quant) >= 10:
        while abs(quant) >= 10:
            quant /= 10
            count += 1
    elif abs(quant) < 1:
        while abs(quant) < 1:
            quant *= 10
            count -= 1
    return [quant, count]
    #print(f'{quant}e{count}')

def exponent_degree_2(quant: float)-> list:
    """определяет значение степени экспоненциального представления числа"""
    count = 0
    flag = True if abs(quant) != quant else False
    quant = abs(quant)
    count = math.floor(math.log10(quant))
    quant = quant / 10 ** count
    quant = quant * (-1) if flag else quant
    return [quant, count]
    #print(f'{quant}e{count}')

def check_exponent_degree(tax: float, new_tax: float):
    """проверка порядка экспоненциального представления после суммы"""
    new_tax += tax
    tax = exponent_degree(tax)
    new_tax = exponent_degree(new_tax)
    if new_tax[1] > tax[1]:
        print('Степень экспоненты суммы увеличилась')
    elif new_tax[1] < tax[1]:
        print('Степень экспоненты суммы уменьшилась')
    else:
        print('Степень экспоненты не изменилась')


num = float(input('Введите бюджет страны: '))
#new_num = float(input('Новые поступления (налог): '))
#check_exponent_degree(num, new_num)

print(exponent_degree_2(num))
