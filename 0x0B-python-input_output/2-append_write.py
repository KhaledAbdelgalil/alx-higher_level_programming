#!/usr/bin/python3
"""
Task: 2. Append to a file
Write a function that appends a
string at the end of a text file
By Khaled Mansour
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file
    and returns the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
