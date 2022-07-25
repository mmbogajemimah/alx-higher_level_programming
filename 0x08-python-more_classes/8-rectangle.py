#!/usr/bin/python3
"""
1-rectangle module
"""


class Rectangle:
    """
    rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

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

        type(self).number_of_instances += 1

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
            p = (2 * self.__height) + (2 * self.__width)
        else:
            p = 0
        return p

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            res = ""
            new_symbol = str(self.print_symbol)
            for row in range(self.__height - 1):
                res += (new_symbol * self.__width) + '\n'
            res += new_symbol * self.__width
        return res

    def __repr__(self):
        h = str(self.__height)
        w = str(self.__width)
        res = "Rectangle(" + w + ", " + h + ")"
        return res

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        pass
