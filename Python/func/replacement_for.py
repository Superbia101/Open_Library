from collections.abc import Iterable
from collections.abc import Iterator


def replacement_for(iter_obj: Iterable) -> None:
    """Эмулирует работу цикла for с помощью цикла while и проходит по всем элементам переданного итерируемого объекта.

    :param iter_obj: Любой итерируемый объект
    :type iter_obj: Iterable

    :except StopIteration: при завершении элементов итерации
    """

    temp: Iterator = iter(iter_obj)

    while True:
        try:
            print(next(temp))
        except StopIteration:
            break




replacement_for([1, 2, 3, 4, 5, 9])
print()
replacement_for((['1'], 2, 'abc', [1, 2], True))
