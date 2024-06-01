from abc import ABC, abstractmethod, override
from typing import List

class Bird(ABC):
    @abstractmethod
    def fly():
        pass

    @abstractmethod
    def walk():
        pass


class Eagle(Bird):
    def fly():
        print("Eagles can fly")

    def walk():
        print("Eagles can walk")


def Penguin(Bird):
    def fly():
        raise Exception("Penguin can't fly")

    def walk():
        print("Penguin can walk")


def shoo_shoo(birds: List[Bird]):
    for bird in birds:
        bird.fly()
        bird.walk()


shoo_shoo([Eagle(), Penguin()])



