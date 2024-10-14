def count_prime_num():
    """Считает количество простых чисел во введённой пользователем последовательности.

    :return: Вывод чисел на экран
    """
    num = int(input('Введите количество чисел: '))
    count: int = 0

    for _ in range(num):
        temp = int(input('Введите целое число: '))
        for quant in range(2, ((temp + 1) // 2) + 1):  # Проверка делителей идёт с 2 до половины+2
            if temp % quant == 0:
                break
        else:
            count += 1

    print('Количество простых чисел в последовательности: ', count)


def prime_num(num: int) -> bool:
    """Проверка переданного числа на принадлежность к простым.

    :param num: arg1
    :type num: int

    :rtype: bool
    :return: flag (True or False)
    """
    for quant in range(2, ((num + 2) // 2) + 1):
        if num % quant == 0:
            flag: bool = False
            break
    else:
        flag = True
    return flag


def prime_num_list(num: int) -> list[int]:
    """Создаёт список из простых чисел до переданного.

    :param num: arg1
    :type num: int

    :rtype: list[int]
    :return: num_list
    """
    num_list: list[int] = []

    for temp in range(2, num + 1):
        for quant in range(2, ((temp + 2) // 2) + 1):
            if temp % quant == 0:
                break
        else:
            num_list.append(temp)
    return num_list


# print(prime_num(int(input('Введите число: '))))
print(prime_num_list(int(input('Введите число: '))))
