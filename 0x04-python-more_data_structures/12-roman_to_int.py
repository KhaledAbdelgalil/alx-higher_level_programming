#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_number = 0
    i = 0
    while i != len(roman_string):
        if i == len(roman_string) - 1 or roman_dict[roman_string[i]] >= roman_dict[roman_string[i + 1]]:
            roman_number = roman_number + roman_dict[roman_string[i]]
        else:
            roman_number = roman_number + roman_dict[roman_string[i + 1]] - roman_dict[roman_string[i]]
            i = i + 1
        i = i + 1
    return roman_number
