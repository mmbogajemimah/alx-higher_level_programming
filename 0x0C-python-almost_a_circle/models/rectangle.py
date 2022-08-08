#!/usr/bin/python3
"""
Rectangle module
"""

from models.base import Base


class Rectangle(Base):
    """
    class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        ...
        """
        super().__init__(id)

        self.check_parameters(width, "width")
        self.check_parameters(height, "height")
        self.check_parameters(x, 'x')
        self.check_parameters(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, parameter):
        """
        width setter
        """
        self.check_parameters(parameter, 'width')
        self.__width = parameter

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, parameter):
        """
        height setter
        """
        self.check_parameters(parameter, 'height')
        self.__height = parameter

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, parameter):
        """
        x setter
        """
        self.check_parameters(parameter, 'x')
        self.__x = parameter

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, parameter):
        """
        y setter
        """
        self.check_parameters(parameter, 'y')
        self.__y = parameter

    def check_parameters(self, value, parameter):
        """
        checks the value of the width, height, x and y
        if they are valid
        """
        if type(value) is not int:
            raise TypeError(parameter + ' must be an integer')
        if value <= 0 and parameter in ('width', 'height'):
            raise ValueError(parameter + ' must be > 0')
        if value < 0 and parameter in ('x', 'y'):
            raise ValueError(parameter + ' must be >= 0')

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the stdout of the rectangle instance with
        the character #
        """
        if self.__height > 0 and self.__width > 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    print("#", end="")
                print()
        else:
            print()

    def __str__(self):
        """
        returns x, y, width, height of rectangle
        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
                self.id, self.x, self.y, self.width, self.height
                )

    def update(self, *args, **kwargs):
        """
        ...
        """
        argc = len(args)
        kwargc = len(kwargs)
        modify_attributes = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5
        if argc > 0:
            for i in range(argc):
                setattr(self, modify_attributes[i], args[i])
        elif kwargc > 0:
            for key, value in kwargs.items():
                if key in modify_attributes:
                    setattr(self, key, value)
