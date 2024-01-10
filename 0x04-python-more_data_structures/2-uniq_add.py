#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    set_list = set(my_list)
    for x in set_list:
        res = res + x
    return res
