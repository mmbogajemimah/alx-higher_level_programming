#!/usr/bin/python3
"""
This validates the kind of class of an object
"""


def is_kind_of_class(obj, a_class):
    """
    Returns true if the object is an instance of
    or if the object is an instance of a class
    from the specified class; otherwise False
    """
    return isinstance(obj, a_class)
