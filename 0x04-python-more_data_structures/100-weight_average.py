#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    divide = 0
    for tuple_item in my_list:
        average += tuple_item[0] * tuple_item[1]
        divide += tuple_item[1]
    return float(average / divide)
