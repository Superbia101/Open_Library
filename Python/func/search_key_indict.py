from typing import Any, Dict, Optional


def search_key_indict(dicts_base: Dict, key_name: Any, key_dep: Optional[int] = None) -> Optional[int]:
    """Находит заданный пользователем ключ в словаре и выдаёт значение соответсвующее ключу,
    возможна настройка глубины поиска.

    :param dicts_base: Словарь в котором производится поиск
    :type dicts_base: Dict
    :param key_name: Искомый ключ
    :type key_name: Any
    :param key_dep: Глубина поиска
    :type key_dep: Optional[int]

    :rtype: Optional[int]
    :return: Возвращает найденное значение или None
    """

    if key_dep is not None:
        if key_dep == 0:
            return
        key_dep -= 1

    if key_name in dicts_base:
        return dicts_base[key_name]

    for in_dicts in dicts_base.values():
        if isinstance(in_dicts, dict):
            target_value = search_key_indict(in_dicts, key_name, key_dep)
            if target_value:
                break
    else:
        target_value = None

    return target_value


if __name__ == '__main__':
    site = {
        'html': {
            'head': {
                'title': 'Мой сайт'
            },
            'body': {
                'h2': 'Здесь будет мой заголовок',
                'div': 'Тут, наверное, какой-то блок',
                'p': 'А вот здесь новый абзац'
            }
        }
    }

    key = input('Введите искомый ключ: ')

    if 'y' == input('Хотите ввести максимальную глубину? Y/N: ').lower():
        val = search_key_indict(site, key, int(input('Введите максимальную глубину: ')))
    else:
        val = search_key_indict(site, key)

    print('Значение ключа:', val)
