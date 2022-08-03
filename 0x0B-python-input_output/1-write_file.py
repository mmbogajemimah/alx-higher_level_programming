#!/usr/bin/python3
"""
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    writes a string to a file or overwrites a
    file if it already exists
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        count_words = f.write(text)
    return count_words
