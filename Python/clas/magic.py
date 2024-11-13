from __future__ import annotations


class Chaos:
    """Базовый для остальных стихий класс "Хаос". Имеет два поля: element, transformation;
    конструктор и метод __add__.
    """
    element: str
    transformation: str | None

    def __init__(self) -> None:
        """Конструктор, создаёт два поля.
        """
        self.element: str = self.__class__.__name__
        self.transformation = None

    def __add__(self, other: type[Chaos]) -> type[Chaos] | type:
        """Метод сложения, оформляет "преобразование" стихий.

        :param other: Второе слагаемое класса Chaos или производного от него (наличие поля element)
        :type other: type

        :rtype: type
        :return: Производный от слагаемых класс
        """
        convergence: set[str] = {self.element, other.element}

        if len(convergence) == 1:
            self.transformation = self.element
            print('{0} + {1} = {2}'.format(self.element, other.element, self.transformation))
            print('А могло быть иначе?')
            return self.__class__

        elif 'Chaos' in convergence:
            self.transformation = 'Chaos'
            print('{0} + {1} = Chaos'.format(self.element, other.element))
            print('Хаос всё обращает в себя!')
            return Chaos

        elif 'Water' in convergence:
            if 'Air' in convergence:
                self.transformation = 'Storm'
            elif 'Fire' in convergence:
                self.transformation = 'Steam'
            elif 'Earth' in convergence:
                self.transformation = 'Mud'

        elif 'Air' in convergence:
            if 'Fire' in convergence:
                self.transformation = 'Lightning'
            elif 'Earth' in convergence:
                self.transformation = 'Dust'

        elif 'Fire' in convergence:
            if 'Earth' in convergence:
                self.transformation = 'Lava'

        print('{0} + {1} = {2}'.format(self.element, other.element, self.transformation))
        return type(self.transformation, (self.__class__, other.__class__), {})


def creation_class(source: type, *args: str) -> list[type]:
    """Создаёт производные классы в количестве переданных имён.

    :param source: Базовый класс
    :type source: type
    :param args: Имена новых классов
    :type args: str

    :rtype: list[type]
    :return: Список производных классов
    """
    return [type(name, (source,), {}) for name in args]


nature = creation_class(Chaos, 'Water', 'Air', 'Fire', 'Earth')
print('Из Хаоса появились стихии их имена на языке Вселенной: {}.'.format(nature))

# nature[1]() + nature[1]()
# nature[1]() + nature[0]()
# nature[0]() + Chaos()
# Chaos() + Chaos()

nature[0]() + nature[1]()
nature[0]() + nature[2]()
nature[0]() + nature[3]()
nature[1]() + nature[2]()
nature[1]() + nature[3]()
print(nature[2]() + nature[3]())
