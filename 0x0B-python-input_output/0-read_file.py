#!/usr/bin/python3
"""
function that reads an input file
"""


def read_file(filename=""):
    """
    reads a file in utf-8 encodinng
    """
    with open('my_file_0.txt', mode="r", encoding="utf-8") as f:
        for line in f:
            print("{}".format(line), end="")
