from abc import ABC, abstractmethod, override
from typing import List

class Bird(ABC):
    @abstractmethod
    def walk():
        pass

class FlyingBird(Bird):
    @abstractmethod
    def fly():
        pass

class Eagle(FlyingBird):
    def walk():
        print("Eagle can walk")

    def fly():
        print("Eagle can fly")


class Penguin(Bird):
    def walk():
        print("Penguin can walk")


def shoo_shoo(birds: List[FlyingBird]):
    for bird in birds:
        bird.walk()
        bird.fly()

shoo_shoo([Eagle()])




## ------------------------------------------------------------------------------------------------------------


class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")

def let_bird_fly(bird: Bird):
    bird.fly()

birds = [Sparrow(), Ostrich()]
for bird in birds:
    let_bird_fly(bird)  # This will break LSP as Ostrich can't fly



























