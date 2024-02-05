#!/usr/bin/python3
"""
Task: 7. Base Geometry
Write a class BaseGeometry
By Khaled Mansour
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer
        Args:
        name (str): name of the parameter
        value (int): value of the parameter to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
