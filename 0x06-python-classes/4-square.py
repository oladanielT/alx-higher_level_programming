#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """Represent a class."""
    def __init__(self, size=0):
        """Initialize a square.
        Args:
            size (int): size of the sqare.
        Raises:
            TypeError: size must be an integer.
            ValueError: size must be greater/equal to 0.
        """
        self.size = size

    def size(self):
        """getting the size value and returning it as a private value"""
        return self.__size

    def size(self, value):
        """
        Initializes size to value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Defines Area of a square.
        Return:
            int: area as integer
        """
        return self.__size ** 2
