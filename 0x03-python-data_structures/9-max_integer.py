#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        result = my_list[0]
        for num in my_list:
            if num > result:
                result = num
        return result
