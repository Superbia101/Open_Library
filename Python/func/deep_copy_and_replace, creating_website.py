from copy import deepcopy

def deep_copy_and_replace(obj: dict, new: str) \
        -> dict | int | float | bool | str | list:
    """Производит глубокое копирование заданного словаря и производит
    замену определённых строк на предоставленную.

    :param obj: arg1 Словарь образец
    :type obj: dict
    :param new: arg2 Замещающая строка
    :type new: str

    :rtype: dict | int | float | bool | str | list
    :return: Рекурсивно возвращает значения,
    общий результат - изменённая глубокая копия
    """
    if isinstance(obj, (int, float, bool, str)):
        if isinstance(obj, str) and ('телефон' in obj or 'iphone' in obj):
            obj = obj.replace('телефон', new).replace('iphone', new)
        return obj
    elif isinstance(obj, list):
        return [deep_copy_and_replace(item, new) for item in obj]
    elif isinstance(obj, dict):
        return {key: deep_copy_and_replace(value, new) for key, value in obj.items()}
    else:
        return deepcopy(obj)


def creating_website(prototype: dict, replace_str: str,
                     list_website: list[dict] = []) -> None:
    """Создаёт и выводит (намеренно введённый mutable list) список созданных макетов.

    :param prototype: arg1
    :type prototype: dict
    :param replace_str: arg2
    :type replace_str: str
    :param list_website: arg3 по умолчанию пустой список
    :type list_website: list[dict]

    :return: Выводит результат на экран
    """
    list_website.append(deep_copy_and_replace(prototype, replace_str))
    print(list_website)



site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
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
