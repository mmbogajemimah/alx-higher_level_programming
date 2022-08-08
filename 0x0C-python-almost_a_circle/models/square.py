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

