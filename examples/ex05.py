'''
Module ex05

Working with abstract classes and methods
'''

from abc import ABC, abstractmethod

class Shape(ABC):
    PI = 3.1416

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius=1.0):
        self.__radius = radius

    @property
    def area(self):
        return self.PI * self.__radius**2

def main():
    c1 = Circle(4.5)
    print('Area of circle is {}'.format(c1.area))

if __name__=='__main__': main()