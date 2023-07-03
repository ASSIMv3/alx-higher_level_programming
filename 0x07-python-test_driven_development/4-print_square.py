#!/usr/bin/python3
"""prints a square with the character #"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for _ in range(size):
            for _ in range(size):
                print("#", end="")
            print("")
