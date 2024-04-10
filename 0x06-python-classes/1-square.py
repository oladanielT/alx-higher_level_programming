#!/usr/bin/python3
"""
Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
"""

class Square:
    """
    size: accessing the size of the square
    __size: making it return a private instance
    """
    def __init__(self, size):
        self.__size = size
