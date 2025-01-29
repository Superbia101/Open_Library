from typing import Dict, Union, Tuple, Any


def find_key(diction: Dict, key: Union[str, int, Tuple]) -> Any:
    """Поиск во вложенном словаре записи по ключу.

    :param diction: Словарь
    :type diction: Dict
    :param key: Искомый ключ
    :type key:  Union[str, int, Tuple]

    :rtype: Any
    :return: Значение ключа
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

    val = find_key(site, input('Искомый ключ: '))
    print(val) if val else print('Такого ключа в структуре сайта нет.')
