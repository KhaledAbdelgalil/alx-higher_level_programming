#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    best_key = -1
    best_value = -1
    for key, value in a_dictionary.items():
        if best_key == -1:
            best_key = key
            best_value = value
        elif value > best_value:
            best_value = value
            best_key = key
    return best_key
