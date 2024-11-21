from typing import Any


class MyDict(dict):
    """
    Производный класс от dict для представления словаря с перегруженным методом get.

    Методы
    ------
    get(key: Any, default: Any =0) -> Any
        Перегруженный метод get
    """

    def get(self, key: Any, default: Any = 0) -> Any:
        """Метод вызова значений словаря по ключу, если ключ отсутствует - значение по умолчанию: 0.

        :param key: Ключ словаря
        :type key: Any
        :param default: Значение по умолчанию при отсутствии ключа
        :type default: Any

        :rtype: Any
        :return: Метод get базового класса с новым значением по умолчанию: 0
        """

        return super().get(key, default)



new_dict: MyDict[str: int] = MyDict()
new_dict['Vik'] = 3
new_dict['Tim'] = 1
print(new_dict)
print(new_dict.get('Mik', 3))
print(new_dict.get('Mik'))
