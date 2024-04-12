#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        initialize square class.
        size (int): size of the square.
        position: position of the square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrieving the value of self"""
        return self.__size

    @size.setter
    def size(self, value):
        """getting the value of size.

        Args:
            value: value of the size.
        Raises:
            TypeError: number must be an integer.
            ValueError: number must be >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integers")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retirving the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """getting the value of our square position"""
        if isinstance(value, tuple):
            if len(value) != 2:
                if not isinstance(value[0], int) and not isinstance(value[1], int):
                    raise TypeError("position must be a tuple of 2 positive integers")
            raise TypeError("position must be a tuple of 2 positive integers")
        raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returning the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """printint to stout thw square with the character #"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
