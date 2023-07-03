#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    i = 0
    while i < len(text):
        if text[i] in [':', '.', '?']:
            print(text[i])
            print("")
            if i < len(text) - 1 and text[i + 1] == " ":
                i += 1
        else:
            print(text[i], end="")
        i += 1
