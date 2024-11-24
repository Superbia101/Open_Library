"""Жадные алгоритмы"""


def continuous_backpack() -> None:
    """Функция выводит максимальную стоимость частей предметов помещающихся в рюкзак,
    с точностью не менее трёх знаков после запятой.
    """

    num_list = []
    value: float = 0
    n, W = [int(i) for i in input('Кол-во предметов и вместимость рюкзака: ').split(' ')]

    for _ in range(n):
        num_list.append([int(i) for i in input('c w: ').split(' ')])

    num_list.sort(key=lambda x: x[0] / x[1], reverse=True)

    for i in range(len(num_list)):
        if num_list[i][1] <= W:
            W -= num_list[i][1]
            value += round(num_list[i][0], 3)
            if W == 0:
                break
        else:
            value += round(num_list[i][0] * W / num_list[i][1], 3)
            break

    print('%.3f' % value)


continuous_backpack()