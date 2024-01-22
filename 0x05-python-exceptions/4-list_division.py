#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    idx = 0
    while idx < list_length:
        try:
            new_list[idx] = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            idx = idx + 1
    return new_list
