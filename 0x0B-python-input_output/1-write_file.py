#!/usr/bin/python3
"""module writes to a file"""


def write_file(filename="", text=""):
    """Write a string to a UTF"""
    with open(filename, encoding="utf-8", mode="w+") as f:
        return f.write(text)
