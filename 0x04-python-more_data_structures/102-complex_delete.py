#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, value_ in a_dictionary.items():
        if value_ == value:
            del a_dictionary[key]
    return a_dictionary

