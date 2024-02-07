#!/usr/bin/python3
"""
Task: 0. Read file [DONE]
Module that reads a text file
(UTF8) and prints it to stdout
By Khaled Mansour
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
