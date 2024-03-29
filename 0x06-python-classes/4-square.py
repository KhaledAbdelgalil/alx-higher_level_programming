#!/usr/bin/python3


"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        '''
        self.size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


''''s = Square(20)
z = s.size
print(z)
print(s.size)
z = 3
print(s.size)
print(z)'''
