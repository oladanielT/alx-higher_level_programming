#!/usr/bin/python3
"""
Defines a square
"""

class Square:
    """ Represent a square class """
    def __init__(self, size=0):
        """
        Initialize a square.

        Args:
            size:Private instance attribute: size.

        Raises:
            TypeError: size must be an integer.
            ValueError: size must be greater than zero.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
