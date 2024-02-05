#!/usr/bin/python3
"""
Task: 8. Rectangle
Write a class Rectangle that defines a rectangle
By Khaled Mansour
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize the Rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
