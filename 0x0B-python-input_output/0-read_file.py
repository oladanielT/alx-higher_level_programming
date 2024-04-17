#!/usr/bin/python3
"""Defines a function"""


def read_file(filename=""):
    """ Function to read a file.

    Parameter:
        filename: files to access.
    """
    with open(filename, encoding='utf-8') as f:
        file_data = f.read()
        print(file_data, end=' ')
