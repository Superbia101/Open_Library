"""список из чисел, которые при делении на 5 дают в остатке 3 

два варианта программы: first и second."""

"""first = [i for i in range(int(input("Ведите предел: "))) if i % 5 == 3]
print(first)
second = [5 * i + 3 for i in range(int(input("Ведите предел: ")))]
print(second)"""

""" можно усложнить"""
#divi - делитель, введённый с клавиатуры
#rem - остаток, введённый с клавиатуры

"""divi = int(input("При делении на что (больше нуля)? "))
rem = int(input("Остаток (должен быть меньше делителя): "))
third = [i for i in range(int(input("Ведите предел: "))) if i % divi == rem]
print(third)"""

""" если нужно определённое кол-во такких чисел"""
#num - кол-во необходимых чисел
#List - список ими заполняемый
#divi - делитель
#rem - остаток
#num - кол-во


def division(divi: int = 2, rem: int = 1, num: int = 10):
    """выводит список из нечётных чисел, с параметрами - чисел с опред. остатком от опред. делителя"""
    list_num: list[int] = []
    if rem >= divi:
        print("Таких чисел не существует!")
    else:
        temp: int = 0 # число для проверки
        while len(list_num) < num:
            temp += 1 # возрастание
            if temp % divi == rem: # проверка на условия
                list_num.append(temp)
        print(list_num)




try:
    divi = int(input("При делении на что (больше нуля)? "))
    rem = int(input("Остаток (должен быть меньше делителя): "))
    num = int(input("Введите кол-во: "))
    division(divi, rem, num)
except:
    print("Должно быть число!")
