#!/usr/bin/python3
"""Module my_int function"""


def add_attribute(obj, attr, value):
    """Function to add a new attribute to an object if possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
