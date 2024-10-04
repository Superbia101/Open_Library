def add_symmetrical_seq(seq_list: list[int]) -> list[int | list[int]]:
    """Определяет минимальное количество и каких чисел надо приписать в
    конец последовательности, чтобы она стала симметричной.

    :param seq_list: arg1
    :type seq_list: list[int]

    :rtype: list[int | list[int]]
    :return: count, temp
    """
    count: int = 0
    temp: list[int] = []

    while seq_list != seq_list[::-1]:
        if seq_list + seq_list[:count + 1][::-1] == seq_list[count::-1][::-1] + seq_list[::-1]:
            temp = seq_list[:count + 1][::-1]
            seq_list.extend(seq_list[:count + 1][::-1])
        count += 1

    return [count, temp]


num_list: list[int] = []

for _ in range(int(input('Кол-во чисел: '))):
    num_list.append(int(input('Число: ')))

print('Последовательность:', num_list)
num, num_list = add_symmetrical_seq(num_list)
print('Нужно приписать чисел:', num)
print('Сами числа:', num_list)
