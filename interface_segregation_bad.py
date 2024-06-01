from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine():
        pass

    @abstractmethod
    def move():
        pass

    @abstractmethod
    def fly():
        pass

class Bicycle(Vehicle):
    def move():
        print("I like to move it move it")

    def start_engine():
        pass

    def fly():
        pass

class Plane(Vehicle):
    def move():
        print("I like to move it move it")

    def start_engine():
        print("it's okay")

    def fly():
        print("I belive I can fly")
