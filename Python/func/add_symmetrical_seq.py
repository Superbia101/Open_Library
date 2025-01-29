from typing import List, Union


def add_symmetrical_seq(seq_list: List[int]) -> List[Union[int, List[int]]]:
    """Определяет минимальное количество и каких чисел надо приписать в
    конец последовательности, чтобы она стала симметричной.

    :param seq_list: Исходная последовательность
    :type seq_list: List[int]

    :rtype: List[Union[int, List[int]]]
    :return: count - количество чисел, temp - их последовательность
    """

    count: int = 0
    temp: List[int] = []

    while seq_list != seq_list[::-1]:
        if (
            seq_list + seq_list[: count + 1][::-1]
            == seq_list[count::-1][::-1] + seq_list[::-1]
        ):
            temp = seq_list[: count + 1][::-1]
            seq_list.extend(seq_list[: count + 1][::-1])
        count += 1

    return [count, temp]


if __name__ == "__main__":
    num_list: List[int] = []

    for _ in range(int(input("Кол-во чисел: "))):
        num_list.append(int(input("Число: ")))

    print("Последовательность:", num_list)
    num, num_list = add_symmetrical_seq(num_list)
    print("Нужно приписать чисел:", num)
    print("Сами числа:", num_list)
