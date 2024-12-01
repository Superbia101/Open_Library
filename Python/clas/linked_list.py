from __future__ import annotations
from collections.abc import Generator
from typing import Any, Optional


class Node:
    """
    Клас для представления элемента односвязного списка.
    """

    __date: Any
    __next: Optional[Node]

    def __init__(self, data: Any) -> None:
        self.__data = data
        self.__next: Optional[Node] = None

    def __str__(self):
        return str(self.data)

    @property
    def data(self) -> Any:
        return self.__data

    @data.setter
    def data(self, new: Any) -> None:
        self.__data = new

    @property
    def next(self) -> Optional[Node]:
        return self.__next

    @next.setter
    def next(self, new: Any) -> None:
        self.__next = new


class LinkedList:
    """
    Класс представляет односвязный список с ячейками класса Node.

    Методы
    ------
    append(new) -> None
        метод добавления элемента в конец списка
    get(target_index: int) -> Any
        метод извлечения значения элемента с заданным индексом
    remove(target_index: int) -> None
        метод удаления из списка элемента с заданным индексом
    """

    __head: Optional[Node]

    def __init__(self) -> None:
        self.__head: Optional[Node] = None

    def __iter__(self) -> Generator[Node]:
        last_node = self.head

        while last_node:
            yield last_node
            last_node = last_node.next

    def __str__(self) -> str:
        return '[{}]'.format(' '.join(map(str, self)))

    @property
    def head(self) -> Optional[Node]:
        return self.__head

    @head.setter
    def head(self, new: Optional[Node]) -> None:
        self.__head = new

    def append(self, new: Any) -> None:
        """Метод добавления элемента, с переданным значением в конец списка.

        :param new: Значение нового элемента
        :type new: Any
        """

        new_node = Node(new)

        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head

            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def get(self, target_index: int) -> Any:
        """Метод извлечения значения элемента из списка по переданному индексу.

        :param target_index: Индекс элемента
        :type target_index: int

        :exception AttributeError: индекс за приделами списка
        :exception AssertionError: индекс отрицательный

        :rtype: Any
        :return: Значение элемента
        """
        try:
            assert target_index >= 0, 'Индекс не может быть отрицательным!'

            last_node = self.head
            node_index = 0

            while node_index < target_index:
                node_index += 1
                last_node = last_node.next
                if node_index == target_index:
                    return last_node.data

        except AttributeError:
            print('Такого индекса в списке нет!')
        except AssertionError as err:
            print(err)

    def remove(self, target_index: int) -> None:
        """Метод удаления элемента из списка по переданному индексу.

        :param target_index: Индекс элемента
        :type target_index: int

        :exception AttributeError: индекс за приделами списка
        :exception AssertionError: индекс отрицательный
        """

        try:
            assert target_index >= 0, 'Индекс не может быть отрицательным!'

            last_node = self.head
            node_index = 0

            while node_index < target_index:
                node_index += 1
                if node_index == target_index:
                    last_node.next = last_node.next.next
                else:
                    last_node = last_node.next

        except AttributeError:
            print('Такого индекса в списке нет!')
        except AssertionError as err:
            print(err)


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

for elem in my_list:
    print(elem)
