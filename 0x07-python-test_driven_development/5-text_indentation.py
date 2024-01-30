#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    idx = 0
    text_len = len(text)
    while idx < text_len and text[idx] == ' ':
        idx += 1

    while idx < text_len:
        print(text[idx], end="")
        if text[idx] == "\n" or text[idx] in ".?:":
            if text[idx] in ".?:":
                print("\n")
            idx += 1
            while idx < text_len and text[idx] == ' ':
                idx += 1
        else:
            idx += 1
