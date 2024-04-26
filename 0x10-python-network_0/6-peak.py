#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(lst):

    """Function that finds a peak in a list of unsorted integers"""
    length = len(lst)
    if length == 0:
        return None

    def get_peak(length, mid):

        if (mid == 0 or lst[mid] >= lst[mid - 1]) \
                and (mid == length - 1 or lst[mid] >= lst[mid + 1]):
            return lst[mid]
        if (mid > 0 and lst[mid - 1] > lst[mid]):
            return get_peak(mid, mid // 2)
        return get_peak(length, mid + (length - mid) // 2)

    return get_peak(length, length // 2)
