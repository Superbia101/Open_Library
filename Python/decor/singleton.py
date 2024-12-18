from typing import Callable, Any, ParamSpec, TypeVar
from functools import wraps


F_Spec = ParamSpec("F_Spec")
F_Return = TypeVar("F_Return")


def singleton(cls: Callable[F_Spec, F_Return]) -> Callable[F_Spec, F_Return]:
    """Декоратор-синглтон, гарантирует, что у класса будет только один экземпляр.

    :param cls: Декорируемый класс
    :type cls: Callable[F_Spec, F_Return]

    :rtype: Callable[F_Spec, F_Return]
    :return: Объект реализации обёртки
    """

    @wraps(cls)
    def wrapper(*args: Any, **kwargs: Any) -> [Callable[..., Any]]:
        """Обёртка для декорируемого класса, осуществляющая создание и регулирование его синглтона.

        :param args: Позиционные аргументы, передаваемые в init класса.
        :type args: Any
        :param kwargs: Именованные аргументы, передаваемые в init класса.
        :type kwargs: Any

        :rtype: Any
        :return: Объект класса
        """

        if not wrapper.flag:
            wrapper.flag = cls(*args, **kwargs)

        return wrapper.flag

    wrapper.flag = None

    return wrapper


@singleton
class Example:
    pass

my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
