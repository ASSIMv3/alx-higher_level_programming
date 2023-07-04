#!/usr/bin/python3
"""prevents the user from dynamically creating new instance attributes
except if the new instance attribute is called first_name"""


class LockedClass:
    """prevents the dynamic creation of new instance attributes,
    except for the attribute 'first_name"""
    __slots__ = ["first_name"]
