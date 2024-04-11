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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def size(self, value):
        """ Setting value """
        self.value = value

    def area(self):
        """Defines Area of a square
        Return:
            int: area.
        """
        return self.__size ** 2
