#!/usr/bin/python3
"""Module my_int function"""


class MyInt(int):
    """MyInt class that inherits from int"""
    def __eq__(self, other):
        """Inverted equality operator"""
        return int(self) != other

    def __ne__(self, other):
        """Inverted inequality operator"""
        return int(self) == other
