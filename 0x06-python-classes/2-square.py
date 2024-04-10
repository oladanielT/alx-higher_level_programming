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
        Instantiation with optional size: def __init__(self, size=0)

        raises:

        TypeError: exception with the message size must be an integer
        ValueError: xception with the message size must be >= 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
