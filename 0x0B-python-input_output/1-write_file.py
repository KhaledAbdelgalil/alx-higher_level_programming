#!/usr/bin/python3
"""
Task: 1. Write to a file
Write a function that writes
a string to a text file
By Khaled Mansour
"""


def write_file(filename="", text=""):
    """Write a string to a text file and return the number of characters written."""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
