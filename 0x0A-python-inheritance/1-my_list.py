#!/usr/bin/python3
"""
Task: 1. My List
Write a class MyList that inherits from list
By Khaled Mansour
"""


class MyList(list):
    """Class MyList that inherits from list"""

    def print_sorted(self):
        """Print the list in ascending order"""
        print(sorted(self))
