#!/usr/bin/python3
"""Define a class square"""

class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        """Initializes a new instance of the Square class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
