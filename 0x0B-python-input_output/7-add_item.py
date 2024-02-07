#!/usr/bin/python3
"""
Task: 7. Add Item
Write a function that adds
an item to a list
By Khaled Mansour
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items.extend(argv[1:])
save_to_json_file(items, filename)
