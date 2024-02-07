#!/usr/bin/python3
"""
Task: 3. To JSON String
Write a function that returns
the JSON representation of an object
By Khaled Mansour
"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object"""
    import json
    return json.dumps(my_obj)
