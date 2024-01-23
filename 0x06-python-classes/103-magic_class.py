#!/usr/bin/python3

"""
Define a MagicClass matching
exactly a bytecode provided by ALX Holberton.
"""

import math


class MagicClass:
    """Represents a circle."""

    def __init__(self, radius=0):
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return (math.pi * (self.__radius ** 2))

    def circumference(self):
        return (2 * math.pi * self.__radius)
