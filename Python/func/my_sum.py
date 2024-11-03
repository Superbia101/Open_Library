def my_sum(*arguments: tuple[int | float | tuple | list | dict]) -> int | float:
    """Складывает числовые значения переданных аргументов.

    :param arguments: *args
    :type arguments: tuple[int | float | tuple | list | dict]

    :raises TypeError: (str | bool | set) как аргумент

    :rtype: int | float
    :return: result
    """
    result: int | float = 0

    for elem in arguments:
        if isinstance(elem, (int, float)):
            result += elem

        elif isinstance(elem, (list, tuple)):
            result += sum(my_sum(in_elem) for in_elem in elem)

        elif isinstance(elem, dict):
            result += sum(my_sum(in_elem) for in_elem in elem.values())

        elif isinstance(elem, (str, bool, set)):
            raise TypeError('Ошибка! Недопустимый тип данных.')

    return result


# print(my_sum([[1, 2, [3]], [1], 3]))
# print(my_sum(1, (1, 1), 3, {1: 2, 2: 2}, [5, 5]))
