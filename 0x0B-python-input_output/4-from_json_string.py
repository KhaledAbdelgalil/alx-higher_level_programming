#!/usr/bin/python3
"""
Task: 4. From JSON string
Write a function that returns an object
represented by a JSON string
By Khaled Mansour
"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string
    """
    return json.loads(my_str)
