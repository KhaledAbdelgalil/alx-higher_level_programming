#!/usr/bin/python3
"""
Task: 11. Student
Write a class Student
that defines a student
By Khaled Mansour
"""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, retrieves only attributes in the list.
        Otherwise, retrieves all attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(str_attr, str) for str_attr in attrs)):
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
        return self.__dict__
