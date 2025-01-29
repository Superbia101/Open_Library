from typing import Tuple


def output_param_func(func, start: int, end: int) -> Tuple[int, float]:
    """max и min значение переданной функции в целочисленных точках диапазона.

    :param func: Переданная функция
    :type func: lambda
    :param start: Нижняя граница диапазона
    :type start: int
    :param end: Верхняя граница диапазона
    :type end: int

    :rtype: Tuple[int, float]
    :return: lisr(max, min)
    """

    if start > end:
        start, end = end, start

    maxx = minn = func(start)

    for i in range(start + 1, end + 1):
        maxx = func(i) if maxx < func(i) else maxx
        minn = func(i) if minn > func(i) else minn

    return maxx, minn


if __name__ == "__main__":
    A = 1
    B = 10
    print(output_param_func(lambda n: 2 * n - 10, A, B))
