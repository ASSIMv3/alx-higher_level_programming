#!/usr/bin/python3
"""Module my_int function"""


class MyInt(int):
    """MyInt class that inherits from int"""
    def __eq__(self, other):
        return super().__ne__(other)
    def __ne__(self, other):
        return super().__eq__(other)
