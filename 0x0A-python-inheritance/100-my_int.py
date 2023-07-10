#!/usr/bin/python3
"""Module my_int function"""


class MyInt(int):
    """MyInt class that inherits from int"""
    def __eq__(self, other):
        """Inverted equality operator"""
        return not (self.real == other.real)
    def __ne__(self, other):
        """Inverted inequality operator"""
        return not (self.real != other.real)
