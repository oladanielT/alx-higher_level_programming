#!/usr/bin/python3
"""Defines a function"""


def read_file(filename=""):
    """Function to read a file"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end=' ')
