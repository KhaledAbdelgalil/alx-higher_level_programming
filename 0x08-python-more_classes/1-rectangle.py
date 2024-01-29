#!/usr/bin/python3


"""Defines a class Rectangle."""


class Square:
    """Represents a Rectangle."""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property width
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property height
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        self.__height = height
