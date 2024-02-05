#!/usr/bin/python3
"""
Task: 3-is_kind_of_class
Write a function that returns True if the object
is an instance of, or if the object is an
instance of a class that inherited from,
the specified class ; otherwise False
By Khaled Mansour
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of,
    or if it's an instance of a class that
    inherited from, the specified class
    """
    return isinstance(obj, a_class)
