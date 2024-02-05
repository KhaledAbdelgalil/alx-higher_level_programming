#!/usr/bin/python3
"""
Task: 0. Lookup
Write a function that returns the list of
available attributes and methods of an object
By Khaled Mansour
"""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return dir(obj)
