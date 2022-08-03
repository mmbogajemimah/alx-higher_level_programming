#!/usr/bin/python3
"""
returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    appends text in a text file
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        count_words = f.write(text)
    return count_words
