from abc import ABC
from abc import abstractmethod
from math import pi


class Shape(ABC):
    """
    Базовый абстрактный класс, представляет геометрическую фигуру.

    Методы
    ------
    area()
        абстрактный метод подсчёта площади фигуры
    """

    @abstractmethod
    def area(self):
        """Абстрактный метод подсчёта площади, который наследники должны переопределить."""

        pass


class Circle(Shape):
    """
    Производный от абстрактного Shape класс, представляет круг.

    Методы
    ------
    area() -> int | float
        переопределённый абстрактный метод подсчёта площади круга
    """

    _radius: int | float

    def __init__(self, value: int | float) -> None:
        self._radius = value

    def area(self) -> int | float:
        """Переопределённый метод для вычисления площади круга.

        :rtype: int | float
        :return: Площадь круга
        """

        return round(pi * self._radius ** 2, 2)


class Rectangle(Shape):
    """
    Производный от абстрактного Shape класс, представляет прямоугольник.

    Методы
    ------
    area() -> int | float
        переопределённый абстрактный метод подсчёта площади прямоугольника
    """

    _length_1: int | float
    _length_2: int | float

    def __init__(self, value_1: int | float, value_2: int | float) -> None:
        self._length_1 = value_1
        self._length_2 = value_2

    def area(self) -> int | float:
        """Переопределённый метод для вычисления площади прямоугольника.

        :rtype: int | float
        :return: Площадь прямоугольника
        """

        return round(self._length_1 * self._length_2, 2)


class Triangle(Shape):
    """
    Производный от абстрактного Shape класс, представляет треугольник.

    Методы
    ------
    area() -> int | float
        переопределённый абстрактный метод подсчёта площади треугольника
    """

    _base: int | float
    _h: int | float

    def __init__(self, value_1: int | float, value_2: int | float) -> None:
        self._base = value_1
        self._h = value_2

    def area(self) -> int | float:
        """Переопределённый метод для вычисления площади треугольника.

        :rtype: int | float
        :return: Площадь треугольника
        """

        return round(0.5 * self._base * self._h, 2)


# Примеры работы с классом:
# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
