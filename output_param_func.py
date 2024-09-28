def output_param_func(func, start: int, end: int) -> list[int | float]:
    """max и min значение переданной функции в целочисленных точках диапазона"""
    if start > end:
        start, end = end, start
    maxx = minn = func(start)
    for i in range(start + 1, end + 1):
        maxx = func(i) if maxx < func(i) else maxx
        minn = func(i) if minn > func(i) else minn
    return [maxx, minn]




L = lambda n: 2 * n - 10
A = 1
B = 10
print(output_param_func(L, A, B))
