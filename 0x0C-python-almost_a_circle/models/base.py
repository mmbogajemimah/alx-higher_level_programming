#!/usr/bin/python3
"""
A model that contains a Base Class.
This class manages all the id attributes that extend from it
thus avoiding duplicating the same code.
"""


class Base:
    """
    manages id attribute in all future classes
    to avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        ...
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
