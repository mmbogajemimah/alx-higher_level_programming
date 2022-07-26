#!/usr/bin/python3
"""
0-add_integer module
"""


def add_integer(a, b=98):
    """
    Adds two numbers after confirming they are integers or floats.
    Casts floats into integers before returning the result.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b 
