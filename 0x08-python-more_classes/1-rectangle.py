#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """Represent my rectangle class"""
    def __init__(self, width=0, height=0):
        """ Initializing the rectangle.

        Parameters:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        Raises:
            TypeError: width and height must be an integer.
            ValueError: width and height must be >= 0.
        """
        self.__width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
