#!/usr/bin/python3
def uppercase(string):
    for char in string:
        uppercase_char = chr(ord(char) - 32) if ord(char) >= 97 and ord(char) <= 122 else char
        print("{}".format(uppercase_char), end="")
        print()
