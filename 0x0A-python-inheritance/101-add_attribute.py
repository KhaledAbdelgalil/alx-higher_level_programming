#!/usr/bin/python3
"""
Task: 13. Can I?
Write a function that adds a new attribute
to an object if possible
By Khaled Mansour
"""


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if possible.

    Args:
        obj: The object to add an attribute to.
        attribute: The name of the attribute to add.
        value: The value to set for the attribute.

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if hasattr(obj, '__dict__') or isinstance(obj, type):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
