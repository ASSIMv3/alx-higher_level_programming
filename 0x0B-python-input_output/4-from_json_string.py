#!/usr/bin/python3
"""from_json_string module"""
import json


def from_json_string(my_str):
    """returns Python objects"""
    return json.loads(my_str)
