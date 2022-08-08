#!/usr/bin/python3
"""
Square Class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    ...
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        ...
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        ...
        """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updating the arguments and the key word arguments
        """
        argc = len(args)
        kwargc = len(kwargs)
        modify_attributes = ['id', 'size', 'x', 'y']

        if argc > 4:
            argc = 4

        if argc > 0:
            for i in range(argc):
                setattr(self, modify_attributes[i], args[i])
        elif kwargc > 0:
            for key, value in kwargs.items():
                if key in modify_attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle
        """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
