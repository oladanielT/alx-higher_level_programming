#!/usr/bin/python3
"""Define a square."""
class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """
        Initialize the square.
        Args:
            size(int): size of the square.
        Raises:
            TypeError: size must be an integer.
            ValueError: size must not be less than o.
        """
        self.__size = size
    def area(self):
        """Defines the area.
        Return:
            int: The area of the square.
        """
        return self.__size ** 2
