#!/usr/bin/python3
for letter in range(26):
    if letter in (4, 16):
        pass
    else:
        print("{:s}".format(chr(letter + 97)), end="")
