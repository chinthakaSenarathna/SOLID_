from abc import ABC, abstractmethod
from socket import socket

class BaseWriter(ABC):
    @abstractmethod
    def write(self, contents: bytearray):
        pass


class FileWriter(BaseWriter):
    def write(self, contents: bytearray):
        with open("random_file.txt", "w") as output_file:
            output_file.write(contents)


class NetworkWriter(BaseWriter):
    def __init__(self) -> None:
        super().__init__()
        self.socket = object()

    def write(self, contents: bytearray):
        self.socket.write(contents)



file_writer = FileWriter()
file_writer.write(b'hello world')

network_writer = NetworkWriter()
network_writer.write(b'hello world')




## -----------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def calculate_areas(shapes):
    for shape in shapes:
        print(shape.area())

shapes = [Circle(2), Rectangle(2, 3)]
calculate_areas(shapes)



























