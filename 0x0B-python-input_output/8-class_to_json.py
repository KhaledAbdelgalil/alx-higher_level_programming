#!/usr/bin/python3
"""
Task: 8. Class to JSON
Write a function that returns
the dictionary description with
simple data structure
"""


def class_to_json(obj):
    """Returns the dictionary description with
    simple data structure for JSON serialization of an object"""
    # Create a dictionary to store object attributes
    obj_dict = {}
    # Iterate through the object's __dict__ to get all attributes
    for key, value in obj.__dict__.items():
        # Check if value is an instance of a simple data structure
        if isinstance(value, (list, dict, str, int, bool)):
            obj_dict[key] = value
        # If it's a complex data structure, you can add additional handling
        # For example, if value is a set, convert it to a list
        elif isinstance(value, set):
            obj_dict[key] = list(value)
        # Add any other custom serializations for other complex types if necessary
        # ...

    return obj_dict
