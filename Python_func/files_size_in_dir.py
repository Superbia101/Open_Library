import os.path


def files_size_in_dir(dirs: str) -> tuple[list, int]:
    """Получает на вход путь до каталога и выводит общее количество файлов и подкаталогов в нём.
    Также выведите на экран размер каталога в килобайтах (1 килобайт = 1024 байт).

    :param dirs: Путь до каталога
    :type dirs: str

    :raises FileNotFoundError: Не существует переданного каталога

    :rtype: tuple[list, int]
    :return: files_list, dirs_num - Кортеж с размерами фалов в килобайтах и кол-во подкаталогов
    """
    if not os.path.exists(dirs):
        raise FileNotFoundError('Ошибка! Такой директории не существует.')

    files_list: list[float] = []
    dirs_num: int = 0

    for content in os.listdir(dirs):
        path: str = os.path.join(dirs, content)
        if os.path.isfile(path):
            files_list.append(os.path.getsize(path) / 1024)
        elif os.path.isdir(path):
            dirs_num += 1
            result: tuple = files_size_in_dir(path)
            if result:
                files_list.extend(result[0])
                dirs_num += result[1]

    return files_list, dirs_num


dir_path = os.path.abspath(os.path.join('..', '..', 'Module14'))
print(dir_path)
size_list, dirs_count = files_size_in_dir(dir_path)
print('Размер каталога (в Кбайтах):', round(sum(size_list), 3))
print('Количество подкаталогов:', len(size_list))
print('Количество файлов:', dirs_count)
