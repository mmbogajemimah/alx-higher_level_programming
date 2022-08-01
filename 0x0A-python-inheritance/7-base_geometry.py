#!/usr/bin/python3
"""
Base Geometry module
"""


class BaseGeometry:
    """
    Defines area method
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates if integer is greater than 0
        and if it is of type int
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
