#!/usr/bin/python3
"""
function that reads an input file
"""


def read_file(filename=""):
    """
    reads a file in utf-8 encodinng
    """
    with open('my_file_0.txt', encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
