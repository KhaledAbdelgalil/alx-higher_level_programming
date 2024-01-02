#!/usr/bin/python3
minus = 0
for letter in range(122, 96, -1):
    print("{:s}".format(chr(letter - minus)), end="")
    if minus == 0:
        minus = 32
    else:
        minus = 0
