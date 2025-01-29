from typing import List, Tuple


def check_ip(ip_address: str) -> bool:
    """Проверяет строку на бытие ip-адресом.

    :param ip_address: Проверяемая строка
    :type ip_address: str

    :rtype: bool
    :return: True | False
    """

    ip_address: List[str] = ip_address.split('.')

    if len(ip_address) == 4 and ''.join(ip_address).isdigit():
        for num in ip_address:
            if not (0 <= int(num) <= 255):
                break
        else:
            return True

    return False


def check_file(file_address: List[str]) -> bool:
    """Проверяет список со строкой на соответствие условиям.

    :param file_address: Список содержащий строку
    :type file_address: List[str]

    :rtype: bool
    :return: True | False
    """

    incorrect_endings: Tuple = '.txt', '.docx'
    special_symbols: Tuple = '@', '№', '$', '%', '^', '&', '*', '(', ')', '\\'
    file_address = ''.join(file_address).split()

    for symbol in file_address:
        if symbol.startswith(special_symbols) or not symbol.endswith(incorrect_endings):
            break

    else:
        return True

    return False


if __name__ == "__main__":
    data = [
        ["128.16.35.a4", ["file_21.txt @data_report.txt notes2024.txt"]],
        ["34.56.42,5", ["file.txt analysis_results.ttx notes2000.txt"]],
        ["128.0.0.255", ["file_1.txt document_2024.docx notes2022.txt"]],
        ["240.127.56.340", ["file_432.txt ^budget_summary.txt notes2021.txt"]],
        ["192.168.1.10", ["file_432.txt  important_info.txt notes1900.txt"]],
        ["192.c8.1.10", ["file_432.xt  &meeting_notes.docx notes1995.txt"]],
        ["10.20.30.40", ["file_432.txt  analysis_results.txt notes1998.txt"]],
    ]
    new_data: list[bool] = [True] * len(data)

    for index, symbol in enumerate(data):
        new_data[index] = check_ip(symbol[0])

    for index, symbol in enumerate(data):
        if new_data[index]:
            new_data[index] = check_file(symbol[1])

    for index, _ in enumerate(data):
        if new_data[index]:
            print(data[index])
