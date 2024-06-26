#!/usr/bin/python3
"""Defines a class module"""


class Rectangle:
    """Represent a class"""
    def __init__(self, width=0, height=0):
        """Initialize a class.
        Parameteres:
            width (int)
            height (int)
        Raises:
            TypeError: number must be integer.
            ValueError: number must be >= 0.
        Return:
            Area (int):
            perimeter (int):
        """
        self.__width = width
        self.__height = height

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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 and self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for i in range(self.__height):
            result += "#" * self.__width + "\n"
        return result
        
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
