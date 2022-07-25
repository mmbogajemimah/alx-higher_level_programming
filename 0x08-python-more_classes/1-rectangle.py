#!/usr/bin/python3
"""
module documentation
"""


class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        if type(height) == int:
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

        if type(width) == int:
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) == int:
                if value >= 0:
                    self.__height = value
                else:
                    raise ValueError("height must be >= 0")
            else:
                raise TypeError("height must be an integer")

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) == int:
                if value >= 0:
                    self.__width = value
                else:
                    raise ValueError("width must be >= 0")
            else:
                raise TypeError("width must be an integer")
