from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move():
        pass


class VehicleWithEngine(Vehicle):
    @abstractmethod
    def start_engine():
        pass


class VehicleWithFly(VehicleWithEngine):
    @abstractmethod
    def fly():
        pass


class Bicycle(Vehicle):
    def move():
        print("I like to move it move it")


class Plane(VehicleWithFly):
    def move():
        print("I like to move it move it")

    def start_engine():
        print("it's okay")

    def fly():
        print("I belive I can fly")
