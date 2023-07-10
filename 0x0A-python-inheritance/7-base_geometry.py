#!/usr/bin/python3
"""Module base_geometry function"""


class BaseGeometry:
    """Base class representing geometry"""
    
    def area(self):
        """Public instance method that raises an Exception with the message"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Public instance method that validates the value"""
        if type(value) != int and type(value) != float:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
