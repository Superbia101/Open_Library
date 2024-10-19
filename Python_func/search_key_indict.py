def search_key_indict(dicts_base: dict, key_name: str | int | bool | tuple,
                      key_dep: int | None = None) -> dict | None:
    """Находит заданный пользователем ключ в словаре и выдаёт значение этого ключа,
    возможна настройка глубины поиска.

    :param dicts_base: arg1 Словарь в котором производится поиск
    :type dicts_base: dict
    :param key_name: arg2 Ключ поиска
    :type key_name: str | int | bool | tuple
    :param key_dep: arg3 Глубина поиска
    :type key_dep: int | None

    :rtype: dict | None
    :return: Возвращает или найденное значение или None
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
