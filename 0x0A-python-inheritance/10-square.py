#!/usr/bin/python3
"""Module square function"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)
