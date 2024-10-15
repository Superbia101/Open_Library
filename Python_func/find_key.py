def find_key(diction: dict, key: str | int | tuple) -> dict | str:
    """Поиск во вложенном словаре записи по ключу.

    :param diction: arg1
    :type diction: dict
    :param key: arg2
    :type key: str | int | tuple

    :rtype:
    :return:
    """
    if key in diction:
        return diction[key]

    for in_diction in diction.values():
        if isinstance(in_diction, dict):
            result = find_key(in_diction, key)
            if result:
                break
    else:
        result = None

    return result


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

val = find_key(site, input('Искомый ключ: '))
print(val) if val else print('Такого ключа в структуре сайта нет.')
