from typing import Callable, Any
from functools import wraps
import datetime

def logging(func: Callable) -> Callable:
    """Декоратор, производит логирование информации переданной функции, её документации
    и обработки ошибок при выполнении.

    При каждом вызове декорируемой функции он выводит на экран её название
    и документацию. В случае возникновения исключения информация об ошибке
    записывается в файл `function_errors.log`.

    :param func: Переданная функция, которую необходимо декорировать
    :type func: Callable

    :rtype: Any
    :return: Ссылка на функцию-обёртку
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Обёртка для декорируемой функции, осуществляющая вывод данных на экран(логирование).

        :param args: Позиционные аргументы, передаваемые в декорируемую функцию.
        :type args: Any
        :param kwargs: Именованные аргументы, передаваемые в декорируемую функцию.
        :type kwargs: Any

        :except Exception: При возникновении исключения, производится запись в файл

        :rtype: Any
        :return: Результат, возвращаемый декорируемой функцией.
        """

        try:
            name = func.__name__
            doc_text = func.__doc__
            print(name)
            print(doc_text)
            return func(*args, **kwargs)

        except Exception as err:
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                print('Ошибка при вызове функции {}.'.format(name))
                file.write('Функция: {0}, ошибка: {1}, время: {2}\n'.format(name, err, datetime.now()))

    return wrapper

def logging_for_class(decorator: Callable) -> Callable:
    """Функция декоратор, для методов класса.

    :param decorator: Используемый декоратор
    :type decorator: Callable

    :rtype: Callable
    :return: Ссылка на функцию-обёртку
    """

    @wraps(decorator)
    def decorate(cls: type) -> type:
        """Функция обёртка, для декоратора класса.

        :param cls: Объект реализации декорируемого класса
        :type cls: type

        :rtype: type
        :return: Объект реализации декорируемого класса, подвергшийся декорации
        """

        for i_method_name in dir(cls):
            if not i_method_name.startswith("__"):
                cur_method = getattr(cls, i_method_name) # извлекаем значение атрибута класса с нужным именем - метод
                decorated_method = decorator(cur_method) # декорируем объект реализации метода
                setattr(cls, i_method_name, decorated_method) # меняем исходный метод на декорированный

        return cls
    return decorate


@logging
@logging_for_class
class Class:
    pass
