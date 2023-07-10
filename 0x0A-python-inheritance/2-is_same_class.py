#!/usr/bin/python3
"""Module is_same_class function"""


def is_same_class(obj, a_class):
    """Compare the type of the object with the specified class"""
    return type(obj) is a_class
