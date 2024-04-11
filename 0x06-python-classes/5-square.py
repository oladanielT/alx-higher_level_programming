#!/usr/bin/python3
"""Defines the square"""


class Square:
    """Represent a square class."""
    def __init__(self, size=0):
        """ Initialize the square.
        size (int): size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """getting the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setting size to value.
        Args:
            value: int to set.
        Raises:
            TypeError: value must be an integer.
            ValueError: value must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size == value

    def area(self):
        """Defines area of the square."""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
