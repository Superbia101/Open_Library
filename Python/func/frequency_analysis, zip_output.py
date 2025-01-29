from zipfile import ZipFile
import os.path


def zip_output(name: str) -> None:
    """Распаковывает в текущий каталог архив.

    :param name: Наименование распаковываемого архива
    :type name: str

    :return: None
    """

    with ZipFile(name) as v_i_m_zip:
        v_i_m_zip.extractall()


def frequency_analysis(name: str) -> None:
    """Выполняет частотный анализ и выводит отсортированный результат в файл analysis.txt.
    Регистр символов учитывается.

    :param name: Наименование анализируемого документа
    :type name: str

    :return: None
    """

    symbol_dict: dict[str: int] = dict()
    symbol_list: list[tuple] = []
    file = open(name, encoding='utf-8')

    for i_line in file:
        for symbol in i_line:
            if symbol.isalpha():
                symbol_dict[symbol] = symbol_dict.get(symbol, 0) + 1

    summ: int = sum(symbol_dict.values())

    for key, val in symbol_dict.items():
        symbol_list.append((key, round(val / summ, 6)))

    del symbol_dict
    symbol_list.sort()
    symbol_list.sort(key=lambda i: i[1], reverse=True)
    wr_file = open('analysis.txt', 'w', encoding='utf-8')
    num: int = 1

    for letter, freq in symbol_list:
        wr_file.write('[{0}] Символ: "{1}" частота: {2}\n'.format(num, letter, freq))
        num += 1

    wr_file.close()


if __name__ == '__main__':
    zipp: str = 'voina-i-mir.zip'  # адрес архива
    file_in_zipp: str = 'voyna-i-mir.txt'  # адрес файла

    if os.path.exists(os.path.abspath(zipp)) and not os.path.exists(os.path.abspath(file_in_zipp)):
        zip_output(zipp)

    if os.path.exists(os.path.abspath(file_in_zipp)):
        frequency_analysis(file_in_zipp)
