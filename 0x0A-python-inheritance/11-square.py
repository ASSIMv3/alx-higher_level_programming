#!/usr/bin/python3
"""Module square function"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
