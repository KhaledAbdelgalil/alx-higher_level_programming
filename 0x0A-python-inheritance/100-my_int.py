#!/usr/bin/python3
"""
Task: 12. My integer
Write a class Square that defines a square
By Khaled Mansour
"""


class MyInt(int):
    """MyInt is a rebel: it inverts == and != operators."""

    def __eq__(self, other):
        """Override equality operator to act as not equal."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override not equal operator to act as equal."""
        return super().__eq__(other)
