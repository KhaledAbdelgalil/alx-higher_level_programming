#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    common_set = set_1.intersection(set_2)
    union_set = set_1.union(set_2)
    return union_set - common_set
