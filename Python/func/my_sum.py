from typing import Any, Union


def my_sum(*arguments: Any) -> Union[int, float]:
    """Складывает значения переданных аргументов. Рекурсивно раскрывает вложения.

    :param arguments: *args
    :type arguments: Any

    :raises TypeError: (str | bool | set) как аргумент

    :rtype: Union[int, float]
    :return: result
    """

    result: Union[int, float] = 0

    for elem in arguments:
        if isinstance(elem, (int, float)):
            result += elem

        elif isinstance(elem, (list, tuple, set)):
            result += sum(my_sum(in_elem) for in_elem in elem)

        elif isinstance(elem, dict):
            result += sum(my_sum(in_elem) for in_elem in elem.values())

        elif isinstance(elem, (str, bool)):
            raise TypeError('Ошибка! Недопустимый тип данных.')

    return result


if __name__ == "__main__":
    print(my_sum([[1, 2, [3]], [1], 3]))
    print(my_sum(1, (1, 1), 3, {1: 2, 2: 2}, [5, 5], {2, 3}))
