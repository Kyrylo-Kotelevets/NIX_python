"""
Напишите скрипт, который вычисляет площадь фигур - прямоугольник, квадрат, треугольник
На входе скрипт принимает название фигуры и длины сторон.
Требования: используйте классы, наследование, модуль sys
"""

from abc import ABC, abstractmethod
from math import sqrt


class Figure(ABC):
    """Basic class for different polygons"""

    @abstractmethod
    def square(self):
        """This method for calculation square"""

    @staticmethod
    @abstractmethod
    def formula():
        """This method return formula for calculating figure square"""


class Square(Figure):
    """Class for triangle"""

    def __init__(self, *sides):
        if len(sides) != 1:
            raise ValueError("Square has only 1 side, got {}".format(len(sides)))
        if not all(isinstance(side, (int, float)) for side in sides):
            raise ValueError("All sides must be numbers")
        if not all(side > 0 for side in sides):
            raise ValueError("All sides must be positive")
        self.a = float(*sides)

    def square(self):
        return self.a * self.a

    @staticmethod
    def formula():
        return "S = a * a"


class Rectangle(Figure):
    """Class for rectangle"""

    def __init__(self, *sides):
        if len(sides) != 2:
            raise ValueError("Rectangle has 2 sides, got {}".format(len(sides)))
        if not all(isinstance(side, (int, float)) for side in sides):
            raise ValueError("All sides must be numbers")
        if not all(side > 0 for side in sides):
            raise ValueError("All sides must be positive")
        self.a, self.b = sides

    def square(self):
        return self.a * self.b

    @staticmethod
    def formula():
        return "S = a * b"


class Triangle(Figure):
    """Class for triangle"""

    def __init__(self, *sides):
        if len(sides) != 3:
            raise ValueError("Triangle has 3 sides, got {}".format(len(sides)))
        if not all(isinstance(side, (int, float)) for side in sides):
            raise ValueError("All sides must be numbers")
        if not all(side > 0 for side in sides):
            raise ValueError("All sides must be positive")
        if (sides[0] >= sides[1] + sides[2]) or \
                (sides[1] >= sides[0] + sides[2]) or \
                (sides[2] >= sides[0] + sides[1]):
            raise ValueError("Can`t solve triangle from sides: {}".format(sides))
        self.a, self.b, self.c = sides

    def square(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    @staticmethod
    def formula():
        return "p = (a + b + c) / 2\nS² = p * (p - a) * (p - b) * (p - c)"


def calculate(figure: str, *sides):
    """function for calculating square from sides anf figure type"""
    if figure.lower() == "square":
        return Square(*sides).square()
    if figure.lower() == "rectangle":
        return Rectangle(*sides).square()
    if figure.lower() == "triangle":
        return Triangle(*sides).square()
    raise ValueError("Unknown figure")


print(calculate('square', 3))
print(calculate('rectangle', 3, 4))
print(calculate('triangle', 3, 4, 5))
