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
        """Обёртка для декорируемой функции, осуществляющая  .

        :param args: Позиционные аргументы, передаваемые в декорируемую функцию.
        :type args: Any
        :param kwargs: Именованные аргументы, передаваемые в декорируемую функцию.
        :type kwargs: Any

        :except Exception: При возникновении исключения, производится запись в файл

        :rtype: Any
        :return: Результат, возвращаемый декорируемой функцией.
        """

        name = func.__name__
        doc_text = func.__doc__
        print(name)
        print(doc_text)
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as err:
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                print('Ошибка при вызове функции {}.'.format({name}))
                file.write('Функция: {0}, ошибка: {1}, время: {2}\n'.format(name, err, datetime.now()))

