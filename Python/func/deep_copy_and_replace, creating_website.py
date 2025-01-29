from copy import deepcopy
from typing import Any, Dict, List


def deep_copy_and_replace(obj: Dict, new: str, old: str) -> Any:
    """Производит глубокое копирование заданного словаря и производит замену определённых строк на предоставленную.

    :param obj: Словарь образец
    :type obj: Dict
    :param new: Замещающая строка
    :type new: str
    :param old: Исходная
    :type old: str

    :rtype: Any
    :return: Рекурсивно возвращает значения, общий результат - изменённая глубокая копия
    """

    if isinstance(obj, (int, float, bool, str)):
        if isinstance(obj, str) and old in obj:
            obj = obj.replace(old, new)
        return obj

    elif isinstance(obj, list):
        return [deep_copy_and_replace(item, new, old) for item in obj]

    elif isinstance(obj, dict):
        return {key: deep_copy_and_replace(value, new, old) for key, value in obj.items()}

    else:
        return deepcopy(obj)


def creating_website(prototype: Dict, replace_str: str, list_website: List[Dict] = []) -> None:
    """Создаёт и выводит (намеренно введённый mutable list) список созданных макетов.

    :param prototype: arg1
    :type prototype: dict
    :param replace_str: arg2
    :type replace_str: str
    :param list_website: arg3 по умолчанию пустой список
    :type list_website: List[Dict]

    :return: Выводит результат на экран
    """

    list_website.append(deep_copy_and_replace(prototype, replace_str, 'iphone'))
    print(list_website)


if __name__ == '__main__':
    site = {
        'html': {
            'head': {
                'title': 'Куплю/продам iphone недорого'
            },
            'body': {
                'h2': 'У нас самая низкая цена на iphone',
                'div': 'Купить',
                'p': 'продать'
            }
        }
    }


    for _ in range(int(input('Сколько сайтов: '))):
        replace_name = input('Введите название продукта для нового сайта: ')
        creating_website(site, replace_name)
