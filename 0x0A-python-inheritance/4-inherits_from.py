#!/usr/bin/python3
"""
Task: 4-inherits_from
Write a function that returns True if the object
is an instance of, or if the object is an
instance of a class that inherited from,
the specified class ; otherwise False
By Khaled Mansour
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
