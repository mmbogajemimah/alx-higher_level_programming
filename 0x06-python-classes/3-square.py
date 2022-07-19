#!/usr/bin/python3
"""
module documentation
"""


class Square:
    """
    Square class
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        answer = self.__size ** 2
        return answer
