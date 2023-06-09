#!/usr/bin/python3
"""class Student module"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return vars(self)
        result = {}
        for attr in attrs:
            if type(attr) is str:
                try:
                    result[attr] = vars(self)[attr]
                except Exception:
                    pass
        return result
