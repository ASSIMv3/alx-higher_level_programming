#!/usr/bin/python3
"""class that inherits from list"""


class MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)