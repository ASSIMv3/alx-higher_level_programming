#!/usr/bin/python3
"""Define a class square"""


class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes and returns the area of the square"""
        return self.__size ** 2
