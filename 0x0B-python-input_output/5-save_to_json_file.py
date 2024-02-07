#!/usr/bin/python3
"""
Task: 5. Save to JSON file
Write a function that writes an Object
to a text file, using a JSON representation
By Khaled Mansour
"""


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation"""
    import json
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
