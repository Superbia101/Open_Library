from collections.abc import Generator
from os import listdir
from os.path import abspath, exists


def str_count_in_dir(str_path: str = abspath('.')) -> Generator[int]:
    """Функция-генератор, берёт все файлы .py в директории и вычисляет количество строк в каждом файле,
    игнорируя пустые строки и строки комментариев.

    :param str_path: Адрес директории
    :type str_path: str

    :except FileNotFoundError: Переданного пути не существует
    :except Exception: Всё остальное

    :rtype: Generator[int]
    :return: Количество строк в очередном файле
    """

    try:
        if not exists(str_path):
            raise FileNotFoundError('Ошибка! Такой директории не существует.')

        for elem in listdir(str_path):
            if elem.endswith('.py'):
                with open(elem) as program:
                    line_list = program.read().split('\n')
                    yield len(line_list) - line_list.count('') - sum((1 for i in line_list if i.startswith('#')))

    except FileNotFoundError as err:
        print(err)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    for file in str_count_in_dir(str_path='..\\01_num_squares'):
        print(file)
