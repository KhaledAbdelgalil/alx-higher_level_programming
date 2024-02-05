#!/usr/bin/python3
"""
Task: 2-is_same_class
Write a function that returns True if the
object is exactly an instance
of the specified class ; otherwise False
By Khaled Mansour
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the specified class."""
    return type(obj) is a_class
