from collections.abc import Iterable
from contextlib import contextmanager
from os import chdir, getcwd, listdir
from os.path import exists


@contextmanager
def сhange_working_directory(new_path: str) -> Iterable:
    """Функция контекст-менеджер, временно меняет текущую рабочую директорию на переданную.

    :param new_path: Абсолютный путь к новой рабочей области
    :type new_path: str

    :return: None
    """

    old_path = getcwd()

    try:
        if not exists(new_path):
            raise FileNotFoundError('Ошибка! Не верный путь!')

        chdir(new_path)

        yield

    except Exception as err:
        print(err)

    finally:
        chdir(old_path)


with сhange_working_directory('C:\\') as a:
    print(listdir())