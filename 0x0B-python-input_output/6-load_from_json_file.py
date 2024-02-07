#!/usr/bin/python3
"""
Task: 6. Load from JSON file
Write a function that
creates an Object from a “JSON file”
By Khaled Mansour
"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
