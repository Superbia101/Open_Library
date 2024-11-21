from __future__ import annotations
from typing import Any


class Stack:
    """
    Класс для представления стека.

    Методы
    ------
    instack(new: Any) -> None
        добавления элемента в стек
    outstack(self) -> Any
        вывод элемента из стека
    __add__(other: Stack) -> str
        сложение стеков
    """

    __value: list[Any]

    def __init__(self) -> None:
        self.__value = []


    @property
    def value(self) -> list[Any]:
        """Геттер атрибута значения стека.

        :rtype: list[Any]
        :return: Значения записанные в стек
        """

        return self.__value


    @value.setter
    def value(self, new: Any) -> None:
        """Сеттер атрибута значения стека.

        :param new: Новое значение
        :type new: Any
        """

        self.__value = new


    def instack(self, new: Any) -> None:
        """Добавление в стек.

        :param new: Новый элемент
        :type new: Any
        """

        self.value.append(new)


    def outstack(self) -> Any:
        """Вывод одного последнего значения из стека.

        :rtype: Any
        :return: Последнее значение в стеке
        """

        return self.value.pop()


    def __str__(self) -> str:
        """Строковое представление экземпляра

        :rtype: str
        :return: Значения атрибута value в виде строки с разделителем и подписью
        """

        return 'Стек: [ {} ]'.format(', '.join([str(elem) for elem in self.value]))


    def __add__(self, other: Stack) -> str:
        """Сложение стеков.

        :param other: Другой стек
        :type other: Экземпляр класса Stack

        :rtype: str
        :return: Строковое представление результата
        """

        self.value.extend(other.value)
        return self.__str__()


class TaskManager:
    """
    Класс для представления менеджера задач, использует экземпляр класса Stack.

    Методы
    ------
    new_task(task: str, priority: int = 0) -> None
        добавления новой задачи, с соответствующим приоритетом
    del_task(task: str) -> tuple | False
        удаляет задачу из стека
    """

    __stack_list: Stack

    def __init__(self) -> None:
        self.__stack_list = Stack()


    @property
    def stack_list(self) -> Stack:
        """Геттер экземпляра стека.

        :rtype: list[Any]
        :return: Значения записанные в стек
        """

        return self.__stack_list

    @stack_list.setter
    def stack_list(self, new: Stack) -> None:
        """Сеттер экземпляра стека.

        :param new: Новое значение
        :type new: Stack
        """

        self.__stack_list = new


    def __check_task(self, task: str) -> int | False:
        """Приватный метод, производит поиск необходимой строки в атрибуте stack_list.

        :param task: Текст задачи
        :type task: str

        :except AssertionError: атрибут task не str

        :rtype: int | False
        :return: Номер задачи в стеке если найдена, False - если нет
        """

        try:
            assert isinstance(task, str), 'Неверный тип данных: атрибут task!'
        except AssertionError as err:
            print(err)
            print('Текст задачи должен быть строкового типа.')
            return False
        else:
            for index, val in enumerate(self.stack_list.value):
                if val[0].lower() == task.lower():
                    return index
            return False


    def new_task(self, task: str, priority: int = 0) -> None:
        """Добавление новой задачи, с соответствующим приоритетом (по умолчанию 0).

        Приватным методом __check_task осуществляется проверка задачи на дубликат.

        :param task: Текст задачи
        :type task: str
        :param priority: Приоритет? значение по умолчанию 0
        :type priority: int

        :except AssertionError: атрибут priority не int
        """

        temp = self.__check_task(task)
        if temp:
            print('Такая задача уже есть: {0} - {1}'.format(self.stack_list.value[temp][1],
                                                            self.stack_list.value[temp][0]))
        else:
            try:
                assert isinstance(priority, int), 'Неверный тип данных: атрибут priority!'
            except AssertionError as err:
                print(err)
                print('Задаче устанавливается приоритет по умолчанию: 0')
                self.stack_list.instack((task, 0))
            else:
                self.stack_list.instack((task, priority))


    def del_task(self, task: str) -> tuple | False:
        """Метод удаления преданной задачи из стека.

        :param task:
        :type task: str

        :rtype: tuple | False
        :return: Если переданная задача в стеке есть удаляет и возвращает кортеж из текста и приоритета, если нет - False
        """

        temp = self.__check_task(task)
        if temp:
            return self.stack_list.value.pop(temp)
        else:
            print('Такой задачи: {} - в стеке нет!'.format(task))
            return False


    def __str__(self) -> str:
        """Строковое представление экземпляра

        :rtype: str
        :return: Задачи оформленные в порядке приоритета
        """

        if len(self.stack_list.value) == 0:
            print('Список задач пуст!')
        else:
            ordered: list[tuple[str, int]] = sorted(self.stack_list.value, key=lambda x: x[1])
            flag: int | None = None

            for index in range(len(ordered)):
                txt: str = ordered[index][0]  # задача для отображения записана
                if ordered[index][1] == flag: # если это задача с уже записанным приоритетом - пропускаем
                    continue
                for elem in range(index + 1, len(ordered)):
                    if ordered[index][1] == ordered[elem][1]:  # если приоритет одинаков
                        txt += '; {}'.format(ordered[elem][0])  # запись задач с общим приоритетом для отображения
                        flag = ordered[index][1]  # идентификатор уже обработанных приоритетов
                    else:
                        break
                print('{0} - {1}'.format(ordered[index][1], txt))

        return ''


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
print(manager)
manager.new_task("сдать ДЗ", 4)
manager.del_task("отдохнуть")
print(manager)
manager.del_task("отдохнуть")
