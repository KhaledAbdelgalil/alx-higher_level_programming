#!/usr/bin/python3
"""
Task: 9. Student
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

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
