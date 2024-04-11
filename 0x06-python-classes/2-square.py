#!/usr/bin/python3
"""Define a square."""

class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """
        Initialize a square.

        Args:
            size (int): getting size of the square.

        Raises:
            TypeError: raise size must be an integer.
            ValueError: raise size must be greater than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
