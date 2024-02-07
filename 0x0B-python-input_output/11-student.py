#!/usr/bin/python3
"""
Task: 11. Student
Write a class Student
that defines a student
By Khaled Mansour
"""


class Student:
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
        if isinstance(
            attrs, list) and all(isinstance(
                item, str) for item in attrs):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from json.
        Assumes json will always be a dictionary with keys as attribute names.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
