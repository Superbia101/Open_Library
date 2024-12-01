from collections.abc import Generator
from os import walk, sep
from os.path import abspath, exists, join


def gen_files_path(desired_dir_name: str, str_path: str = abspath(sep)) -> Generator[str]:
    """Функция-генератор которая рекурсивно проходит по всем каталогам (включая вложенные папки и подпапки) указанной
    директории (по умолчанию — корневой диск), находит указанный пользователем каталог и генерирует пути всех
    встреченных файлов.

    :param desired_dir_name: Имя искомого каталога
    :type desired_dir_name: str
    :param str_path: Путь поиска (по умолчанию корневой диск)
    :type str_path: str

    :except FileNotFoundError: Переданного пути поиска не существует.

    :rtype: Generator[str]
    :return: Генератор абсолютных адресов всех встреченных файлов.
    """

    try:
        if not exists(str_path):
            raise FileNotFoundError('Ошибка! Такой директории не существует.')

        for dir_path, dir_names, files in walk(str_path):

            for elem in files:
                yield join(dir_path, elem)

            if desired_dir_name in dir_names:
                break

    except FileNotFoundError as err:
        print(err)
    except Exception as err:
        print(err)


for i in gen_files_path('User', ):
    print(i)
