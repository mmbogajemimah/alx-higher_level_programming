#!/usr/bin/python3
"""
1-rectangle module
"""


class Rectangle:
    """
    rectangle class
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

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height != 0 and self.__width != 0:
            peri = (2 * self.__height) + (2 * self.__width)
        else:
            peri = 0
        return peri

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            result = ""
            for i in range(self.__height - 1):
                result += ("#" * self.__width) + '\n'
            result += "#" * self.__width
        return result

    def __repr__(self):
        height = str(self.__height)
        width = str(self.__width)
        result = "Rectangle(" + width + ", " + height + ")"
        return result
