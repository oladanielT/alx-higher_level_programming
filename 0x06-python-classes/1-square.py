#!/usr/bin/python3
"""
Square module.

Defines a square by:
- Private instance attribute: size
- Instantiation with size (no type/value verification)
You are not allowed to import any module
"""

class Square:
    """
    Square class.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
