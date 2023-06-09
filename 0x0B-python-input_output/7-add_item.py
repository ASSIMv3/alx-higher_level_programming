#!/usr/bin/python3
"""add_item module"""
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    ls = load_from_json_file("add_item.json")
except FileNotFoundError:
    ls = []

for i in range(1, len(sys.argv)):
    ls.append(sys.argv[i])
save_to_json_file(ls, "add_item.json")
