from typing import Callable, Any, ParamSpec, TypeVar
from functools import wraps
from time import time
from datetime import datetime


F_Spec = ParamSpec("F_Spec")
F_Return = TypeVar("F_Return")


def log_methods(form: str) -> Callable[..., Any]:
    """Функция передачи декоратору парамера.

    :param form: Формат даты и времени вывода логов.
    :type form: str

    :rtype: Callable[..., Any]
    :return: Объект реализации обёртки
    """

    def log(func: Callable[F_Spec, F_Return], cls: Callable[..., Any]) -> Callable[F_Spec, F_Return]:
        """Декоратор, выводит логи запуска методов класса, по определённому шаблону.

        :param func: Переданный метод
        :type func: Callable[F_Spec, F_Return]
        :param cls: Класс, которому принадлежит метод. Используется для логирования.
        :type cls: Callable[..., Any]

        :rtype: Callable[F_Spec, F_Return]
        :return: Объект реализации обёртки декоратора
        """

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Обёртка для декорируемой функции, осуществляющая вывод логов по выбранному шаблону.

            :param args: Позиционные аргументы, передаваемые в декорируемую функцию.
            :type args: Any
            :param kwargs: Именованные аргументы, передаваемые в декорируемую функцию.
            :type kwargs: Any

            :rtype: Any
            :return: Результат работы переданной функции
            """

            new_form = ''.join(['%{}'.format(elem) if elem.isalpha() else str(elem) for elem in form])
            now = datetime.now()
            formatted_date = now.strftime(new_form)
            print('Запускается {0}. Дата и время запуска: {1}.'.format(cls.__name__, formatted_date))
            started_time = time()
            result = func(*args, **kwargs)
            ended_time = time()
            func_time = ended_time - started_time
            print(
                "Завершение '{0}.{1}', время работы = {2} s.".format(cls.__name__, func.__name__, round(func_time, 3)))

            return result

        return wrapper

    def decorate(cls: [Callable[..., Any]]) -> Callable[..., Any]:
        """Функция выбирающая методы переданного класса и декорирующая их.

        :param cls: Переданный класс
        :type cls: [Callable[..., Any]]

        :rtype: [Callable[..., Any]]
        :return: Декорированный класс
        """

        for method_name in dir(cls):
            if not method_name.startswith("__"):
                cur_method = getattr(cls, method_name) # извлекаем значение атрибута класса с нужным именем - метод
                decorated_method = log(func=cur_method, cls=cls) # декорируем объект реализации метода
                setattr(cls, method_name, decorated_method) # меняем исходный метод на декорированный

        return cls

    return decorate


@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")


    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
