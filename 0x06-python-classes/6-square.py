#!/usr/bin/python3


"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        '''
        self.size = size
        self.position = position

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

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not self.validate_position(value):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value

    def validate_position(self, position):
        cond = isinstance(position, tuple)
        '''print(condition)'''
        if not cond:
            return False
        cond = len(position) == 2
        '''print(condition)'''
        if not cond:
            return False
        cond = all(isinstance(coord, int) and coord >= 0 for coord in position)
        '''print(condition)'''
        if not cond:
            return False
        return True


'''
my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
'''
