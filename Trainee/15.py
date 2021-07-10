"""
Создайте несколько классов: Animal (абстрактный класс), Cat, Dog
Создайте абстрактные методы say, run и jump в классе Animal (abc.abstractmethod)
Реализуйте полиморфизм поведения животных для методов: say, run, jump
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class for creating different animals"""
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def say(self):
        """Method for speaking"""

    @abstractmethod
    def run(self):
        """Method for running"""

    @abstractmethod
    def jump(self):
        """Method for jumping"""


class Cat(Animal):
    """Class for usual cat instance"""

    def say(self):
        return "{} says meow".format(self.name)

    def run(self):
        return "{} runs away from the vacuum cleaner".format(self.name)

    def jump(self):
        return "{} jumping on the kitchen table".format(self.name)

    def __str__(self):
        return "Hello, my name is {} I am a cat".format(self.name)


class Dog(Animal):
    """Class for usual dog instance"""

    def say(self):
        return "{} says woof".format(self.name)

    def run(self):
        return "{} runs for a walk".format(self.name)

    def jump(self):
        return "{} jumping into the biggest puddle".format(self.name)

    def __str__(self):
        return "Hello, my name is {} I am a dog".format(self.name)


for animal in (Cat("Barsic"), Dog("Sharic")):
    print(animal)
    print(animal.say())
    print(animal.run())
    print(animal.jump())
